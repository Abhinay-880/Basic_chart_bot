import spacy
import matplotlib.pyplot as plt

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

def generate_chart(data):
    labels = list(data.keys())
    values = list(data.values())

    plt.bar(labels, values)
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Bar Chart')
    plt.show()

def extract_data(input_text):
    data = {}
    doc = nlp(input_text)

    for ent in doc.ents:
        if ent.label_ == 'PRODUCT':
            category = ent.text
        elif ent.label_ == 'CARDINAL':
            value = float(ent.text)
            data[category] = value

    return data

def main():
    print("Welcome to the Basic Chart Bot!")
    print("Please provide data for the chart.")

    input_text = input("Enter your data: ")

    data = extract_data(input_text)

    if data:
        generate_chart(data)
    else:
        print("No relevant data found for chart generation.")

if __name__ == "__main__":
    main()
