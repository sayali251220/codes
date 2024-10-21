import numpy as np

def rgb_to_grayscale(rgb_image):
    # Using standard grayscale conversion formula: 0.2989 * R + 0.5870 * G + 0.1140 * B
    grayscale_image = np.dot(rgb_image[..., :3], [0.2989, 0.5870, 0.1140])
    return grayscale_image

def apply_threshold(grayscale_image, threshold):
    # Applying the threshold to convert to binary image
    binary_image = np.where(grayscale_image > threshold, 255, 0)
    return binary_image

def get_image_input():
    height = int(input("Enter the height of the image: "))
    width = int(input("Enter the width of the image: "))
    image = np.zeros((height, width, 3), dtype=int)

    print(f"Enter RGB values for {height}x{width} image:")
    for i in range(height):
        for j in range(width):
            r = int(input(f"Enter red value for pixel ({i}, {j}): "))
            g = int(input(f"Enter green value for pixel ({i}, {j}): "))
            b = int(input(f"Enter blue value for pixel ({i}, {j}): "))
            image[i, j] = [r, g, b]

    return image

def main():
    while True:
        print("\nChoose an option:")
        print("1. Grayscale Conversion")
        print("2. Apply Threshold for Binary Conversion")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1 or choice == 2:
            rgb_image = get_image_input()
            grayscale_image = rgb_to_grayscale(rgb_image)

            if choice == 1:
                print("Grayscale Image:\n", grayscale_image)
            elif choice == 2:
                try:
                    threshold = int(input("Enter threshold value (0-255): "))
                except ValueError:
                    print("Invalid threshold value! Please enter an integer between 0 and 255.")
                    continue

                binary_image = apply_threshold(grayscale_image, threshold)
                print("Binary Image:\n", binary_image)
        
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
