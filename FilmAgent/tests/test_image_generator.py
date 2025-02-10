import os
import json
import pytest
from unittest.mock import patch, mock_open, MagicMock
from PIL import Image
from FilmAgent.image_generator import generate_images_from_script, create_output_directory, generate_image_with_text

# Constants for testing
MOCK_OUTPUT_DIR = "./test_generated_images"
MOCK_FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
MOCK_SCRIPT_PATH = "./mock_script.json"
MOCK_INTERVAL = 5

@pytest.fixture
def setup_environment(monkeypatch, tmp_path):
    """
    Fixture to set up the environment for testing.
    """
    # Mock environment variables
    monkeypatch.setenv("IMAGE_OUTPUT_DIR", str(tmp_path / "generated_images"))
    monkeypatch.setenv("FONT_PATH", MOCK_FONT_PATH)
    monkeypatch.setenv("SCRIPT_PATH", MOCK_SCRIPT_PATH)
    monkeypatch.setenv("IMAGE_INTERVAL", str(MOCK_INTERVAL))

    # Create the output directory
    os.makedirs(tmp_path / "generated_images", exist_ok=True)

    # Return the temporary path for further use
    return tmp_path

def test_create_output_directory(setup_environment):
    """
    Test that the output directory is created successfully.
    """
    output_dir = os.getenv("IMAGE_OUTPUT_DIR")
    assert not os.path.exists(output_dir)  # Ensure directory doesn't exist initially
    create_output_directory()
    assert os.path.exists(output_dir)  # Directory should be created

@patch("FilmAgent.image_generator.Image.save")
def test_generate_image_with_text(mock_save, setup_environment):
    """
    Test that an image is generated with the correct text and filename.
    """
    output_dir = os.getenv("IMAGE_OUTPUT_DIR")
    filename = os.path.join(output_dir, "test_image.png")
    text = "Test Text"

    # Generate the image
    generate_image_with_text(text, filename)

    # Verify that the image was saved
    mock_save.assert_called_once_with(filename)

    # Verify the image content
    image = Image.open(mock_save.call_args[0][0])
    assert image.size == (800, 600)  # Default dimensions
    assert image.mode == "RGB"  # Default mode

@patch("builtins.open", new_callable=mock_open, read_data=json.dumps([
    {"duration": 10}, {"duration": 15}, {"duration": 20}
]))
@patch("FilmAgent.image_generator.generate_image_with_text")
def test_generate_images_from_script(mock_generate_image, mock_open_file, setup_environment):
    """
    Test that images are generated correctly based on the script and interval.
    """
    script_path = os.getenv("SCRIPT_PATH")
    interval = int(os.getenv("IMAGE_INTERVAL"))
    output_dir = os.getenv("IMAGE_OUTPUT_DIR")

    # Generate images
    generated_images = generate_images_from_script(script_path, interval)

    # Verify the number of images generated
    total_duration = 10 + 15 + 20  # Sum of durations in the mock script
    expected_num_images = total_duration // interval
    assert len(generated_images) == expected_num_images

    # Verify filenames and calls to generate_image_with_text
    for i, filename in enumerate(generated_images):
        sequence_index = i + 1
        expected_filename = os.path.join(output_dir, f"image_{sequence_index:03d}.png")
        assert filename == expected_filename
        mock_generate_image.assert_any_call(f"Timestamp: {sequence_index * interval}s", expected_filename)

def test_generate_images_consistency(setup_environment):
    """
    Test that running the generator multiple times with the same script produces identical filenames.
    """
    with patch("builtins.open", new_callable=mock_open, read_data=json.dumps([
        {"duration": 30}
    ])):
        generated_images_run1 = generate_images_from_script(MOCK_SCRIPT_PATH, 10)
        generated_images_run2 = generate_images_from_script(MOCK_SCRIPT_PATH, 10)
        assert generated_images_run1 == generated_images_run2
        expected_filenames = [
            os.path.join(MOCK_OUTPUT_DIR, "image_001.png"),
            os.path.join(MOCK_OUTPUT_DIR, "image_002.png"),
            os.path.join(MOCK_OUTPUT_DIR, "image_003.png"),
        ]
        assert generated_images_run1 == expected_filenames
    # Case 1: Zero duration
    with patch("builtins.open", new_callable=mock_open, read_data=json.dumps([])):
        generated_images = generate_images_from_script(MOCK_SCRIPT_PATH, MOCK_INTERVAL)
        assert len(generated_images) == 0  # No images should be generated

    # Case 2: Very short interval
    with patch("builtins.open", new_callable=mock_open, read_data=json.dumps([
        {"duration": 1}, {"duration": 2}
    ])):
        generated_images = generate_images_from_script(MOCK_SCRIPT_PATH, 1)
        assert len(generated_images) == 3  # One image per second

    # Case 3: Interval longer than total duration
    with patch("builtins.open", new_callable=mock_open, read_data=json.dumps([
        {"duration": 5}
    ])):
        generated_images = generate_images_from_script(MOCK_SCRIPT_PATH, 10)
        assert len(generated_images) == 0  # No images should be generated

    # Case 4: Verify sequential filenames for a short script
    with patch("builtins.open", new_callable=mock_open, read_data=json.dumps([
        {"duration": 15}
    ])):
        generated_images = generate_images_from_script(MOCK_SCRIPT_PATH, 5)
        expected_filenames = [
            os.path.join(MOCK_OUTPUT_DIR, "image_001.png"),
            os.path.join(MOCK_OUTPUT_DIR, "image_002.png"),
            os.path.join(MOCK_OUTPUT_DIR, "image_003.png"),
        ]
        assert generated_images == expected_filenames

@patch("FilmAgent.image_generator.os.makedirs")
def test_create_output_directory_already_exists(mock_makedirs, setup_environment):
    """
    Test that create_output_directory does not raise an error if the directory already exists.
    """
    output_dir = os.getenv("IMAGE_OUTPUT_DIR")
    os.makedirs(output_dir, exist_ok=True)  # Create the directory beforehand
    create_output_directory()
    mock_makedirs.assert_called_once_with(output_dir, exist_ok=True)