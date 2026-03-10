from google import genai


def get_response(content):
    client = genai.Client(api_key="Your api key")

    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=content
    )

    return response.text

animal = get_response("Randomely choose an animal from the animal kingdom and only give me the name of the animal no need to give description or anything just give me the name of that animal ")
final_score = 10
for i in range(10):
    question = input(f"Enter your {i+1} question: ")
    final_score -= 1
    answer = get_response(f""" The user is trying to guess {animal} and is asking questions about it from you you can only give answer of 1 line do not go into detials
                        give simple answers required question do not go into the detail the question asked by the user is {question} and if both question and the animal matches
                        then reply with you got it only when the animal matches with the question if i get some question correct do not reply with you got it only reply it when
                        i guess the animal write you got it is strictly for it """)
    if "you got it." in answer.lower():
        print(f"You guessed the animal correctly indeed it was {animal} and your final score is : {final_score}")
        break
    else:
        print(answer)

if final_score == 0:
    print(f"You lost the correct answer was {animal}")