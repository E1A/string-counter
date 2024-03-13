import argparse

def most_used_string(file_path):
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the content of the file
        content = file.read()

    # Split the content into words
    words = content.split()

    # Create a dictionary to store the count of each word
    word_count = {}

    # Iterate through each word
    for word in words:
        # Remove any punctuation from the word
        word = word.strip('.,!?;:"\'').lower()

        # If the word is already in the dictionary, increment its count
        if word in word_count:
            word_count[word] += 1
        # If the word is not in the dictionary, add it with a count of 1
        else:
            word_count[word] = 1

    # Sort the dictionary items by their values (counts)
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    # Return the sorted word count
    return sorted_word_count

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Find the most used string(s) in a file.')

    # Add arguments
    parser.add_argument('-l', '--file_path', type=str, help='Path to the file')

    # Parse the command line arguments
    args = parser.parse_args()

    # Check if the file path is provided
    if args.file_path:
        # Call the function to find the most used string(s)
        sorted_word_count = most_used_string(args.file_path)

        # Print the overview
        print("Most used string(s):")
        for string, count in sorted_word_count:
            print(f"{count} - {string}")

    else:
        print("Please provide the path to the file using the -l or --file_path option.")

if __name__ == "__main__":
    main()
