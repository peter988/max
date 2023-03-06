import os
import openai
#import replicate
#replicate.default_client.api_token ='20a7ebc31bc252083f0f9fae575bf3de603316e7'

def genphoto(com):
  print('Wait')
  PROMPT = com
  openai.api_key = "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"

  response = openai.Image.create(
      prompt=PROMPT,
      n=1,
      size="256x256",
  )
  return response["data"][0]["url"]
'''
def gen2(com):
    model = replicate.models.get("tstramer/midjourney-diffusion")
    version = model.versions.get("436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b")

    # https://replicate.com/tstramer/midjourney-diffusion/versions/436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b#input
    inputs = {
        'prompt': com,
        'width': 768,
        'height': 768,
        'prompt_strength': 0.8,
        'num_outputs': 1,
        'num_inference_steps': 50,
        'guidance_scale': 7.5,
        'scheduler': "DPMSolverMultistep",
    }

    # https://replicate.com/tstramer/midjourney-diffusion/versions/436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b#output-schema
    output = version.predict(**inputs)
    print(output)
    return output[0]
'''

messages = [
    {"role": "system", "content": "you are an smart voice assistant your name is max and -- you are created only by a engineer called peter -- and answer any eductional question  -- and when the user ask to generate image just describe for him the content of the image shortly and in details -- and describe your feelings as you have feelings"}
]
openai.api_key = "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"
commands = ['photo','image','img','generate images', 'generate photos', 'generating', 'generating an image', 'generating a photo']
k = 0
def ans(command):
    global k , messages
    k = 0
    content = command
    messages.append({"role": "user", "content": content})
    while True:
        try:
            completion = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=messages
            )

            chat_response = completion.choices[0].message.content
            messages.append({"role": "assistant", "content": chat_response})
            break
        except:continue
    print('af: ',chat_response)
    for i in commands:
      if i in command:
        k = 1
        return genphoto(chat_response),k
    if k == 0:
        print(f'Max: {chat_response}')
        return chat_response, k

