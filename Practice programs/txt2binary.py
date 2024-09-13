def text_to_binary(text):

  binary_result = ' '.join(format(ord(char), '08b') for char in text)

  return binary_result



def main():

  user_input = input("Enter text: ")

  binary_output = text_to_binary(user_input)

  print(binary_output)



if __name__ == "__main__":

  main()