import requests
import base64
url = "http://localhost:7861/sdapi/v1"
class Test:
    def __init__(self):
        self.url = url

    def get_models(self):
        response = requests.get(f"{self.url}/sd-models")
        return response.json()
    def text_to_image(self, prompt, negative_promt):
        payload = {
            "prompt": prompt,
            "negative_prompt": negative_promt,
            "steps": 20,
            "override_settings": {
                "sd_model_checkpoint": "realisticVisionV13_v13"
            }
        }
        response = requests.post(f"{self.url}/txt2img", json=payload)
        return response.json()



if __name__ == "__main__" :
    import os
    os.environ["PYTORCH_MPS_HIGH_WATERMARK_RATIO"] = "0.0"
    test = Test()
    # print(test.get_models())
    image_binary = test.text_to_image("Speedpainting (Glamour:1.3) Photo of (Icelandic:1.2) Beauty Queen Edda Jørgensen Medium rich (Auburn Red Hair) Stylish haircut, (Pale skin tone, clear complexion:0.9), Lengthened Rectangular Face with Gentle Jaw and Cheekbones, Rounded Eyebrows, Deep-Set Upturned Eyes, Brown Hazel Eyes, Natural Straight Nose, Refined Thin Lips, Rapturous Beam , (Hourglass figure:1.1),(large breasts:1.2), (cleavage:1.1), Wearing a metallic copper satin and black lace teddy, channeling the glamorous and seductive style of Dolce & Gabbana,,  skindentation, (Close up:1.3), lounging in Boudoir,(Cinematic Lighting), From Above  Shot using a (Canon P Camera:1.3), using a (50mm f/1.8 lens:1.3), on (Fujicolor film:1.3), in the style of (Vivian Maier:1.3)", "(badhandv4:1.3) (worst quality, low quality, normal quality:1.2), painting, drawing, monochrome, grayscale, bad anatomy, bad proportions, (camera:1.3), (signature, watermark:1.2),( hourglass:1.2),, EasyNegativeV2 , BadDream,  structurezoov15,")
    # wb means write binary
    with open("output.png", "wb") as f:
        f.write(base64.b64decode(image_binary["images"][0]))


