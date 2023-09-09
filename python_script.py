import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python python_script.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]

    # Perform image processing here
    # Replace this with your actual image processing code

    # For example, let's just display a message
    print(f"Image processing completed for {image_path}")
