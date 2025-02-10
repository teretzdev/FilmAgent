import os
import argparse
from util import read_prompt, write_json
from LLMCaller import GPTCall, clean_text, GPTResponse2JSON

def generate_actor_scripts(input_file: str, output_dir: str):
    """
    Generate actor scripts based on text prompts from an input file.

    Args:
        input_file (str): Path to the input file containing text prompts.
        output_dir (str): Directory where the generated scripts will be saved.

    Returns:
        None
    """
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read the input prompts
    try:
        prompts = read_prompt(input_file)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return
    except Exception as e:
        print(f"Error reading input file: {e}")
        return

    # Generate scripts for each prompt
    generated_scripts = []
    for idx, prompt in enumerate(prompts):
        print(f"Processing prompt {idx + 1}/{len(prompts)}...")
        try:
            # Call the AI model to generate the script
            raw_response = GPTCall(prompt)
            cleaned_response = clean_text(raw_response)
            script = GPTResponse2JSON(cleaned_response)
            generated_scripts.append(script)
        except Exception as e:
            print(f"Error generating script for prompt {idx + 1}: {e}")
            continue

    # Save the generated scripts to the output directory
    output_file = os.path.join(output_dir, "generated_actor_scripts.json")
    try:
        write_json(output_file, generated_scripts)
        print(f"Generated scripts saved to '{output_file}'.")
    except Exception as e:
        print(f"Error saving generated scripts: {e}")

def main():
    """
    Main function to parse command-line arguments and trigger script generation.
    """
    parser = argparse.ArgumentParser(description="Generate actor scripts based on text prompts.")
    parser.add_argument(
        "-i", "--input", required=True, help="Path to the input file containing text prompts."
    )
    parser.add_argument(
        "-o", "--output", required=True, help="Directory where the generated scripts will be saved."
    )
    args = parser.parse_args()

    generate_actor_scripts(args.input, args.output)

if __name__ == "__main__":
    main()
