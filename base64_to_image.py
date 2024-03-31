import base64util
import argparse

BANNER = "\nBase64 to Image\n"
EXTENSIONS_BASE64 = ['.txt']
EXTENSIONS_IMAGE = ['.png', '.jpg', '.jpeg']


def main():
    parser = argparse.ArgumentParser(description='Convert Base64 to Image')
    parser.add_argument("--input", type=str, help="Base64 Path (input)")
    parser.add_argument("--output", type=str, help="Image Path (output)")
    args = parser.parse_args()

    print(BANNER)
    try:
        if not args.input:
            base64_path = input("Please enter the path of the Base64 you want to convert to Image: ")
        else:
            base64_path = args.input

        if not base64util.validate_file_path(base64_path, EXTENSIONS_BASE64):
            print(f"ERROR: Invalid Base64 path: {base64_path}")
        else:
            image = base64util.base64_to_image(base64_path)

            if not args.output:
                output_file_path = input("\n\nEnter the output file path to save the Image: ")
            else:
                output_file_path = args.output

            if not base64util.validate_file_extension(output_file_path, EXTENSIONS_IMAGE):
                print(f"ERROR: Invalid output path: {output_file_path}")
            else:
                base64util.save_image_to_file(image, output_file_path)

                print(f"\n\nThe Image was saved to '{output_file_path}'.")

    except FileNotFoundError:
        print("ERROR: Invalid Path!")


if __name__ == "__main__":
    main()
