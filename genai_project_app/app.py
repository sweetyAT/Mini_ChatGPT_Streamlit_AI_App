from transformers import pipeline

# Load a small text generation model from Hugging Face
generator = pipeline("text-generation", model="gpt2")

print(" Mini-ChatGPT is ready! Type your prompt below.")
print("Type 'exit' to quit.\n")

while True:
    prompt = input("You: ")

    if prompt.lower() == "exit":
        print("👋 Goodbye!")
        break

    response = generator(prompt, max_length=60, num_return_sequences=1)
    print("AI:", response[0]["generated_text"])
    print()
