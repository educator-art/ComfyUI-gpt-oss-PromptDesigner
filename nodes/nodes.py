"""
usage system:
- Google Colab L4 GPU 
    - option: High Memory

note:
Google Colab has the OpenAI library installed.
openai 1.99.1 (Checked: 2025.08.11)
"""
from openai import OpenAI

system_prompt="""You are Stable Diffusion Prompt Designer."""

user_prompt="""# 依頼
以下の条件に従ってプロンプトを英語で作成してください

## プロンプトのテーマ
美しい風景

## 単語数
30単語程度

## Output
"""

class LoadGPTOSSPromptDesigner:

    def __init__(self):

        self.system_prompt=""
        self.user_prompt=""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "system": (
                    "STRING",
                    {"multiline": False, "default": system_prompt},
                ),
                "user": (
                    "STRING",
                    {"multiline": True, "default": user_prompt},
                ),
            },
        }

    # After Inference, Default output: "Stable Diffusion Prompt"
    RETURN_TYPES = ("STRING",)
    FUNCTION = "inference"
    OUTPUT_NODE = True
    CATEGORY = "Load gpt-oss Prompt Designer"

    def inference(self, system, user):

        # if text is empty, display error
        if not system:
            raise ValueError(f"system promptが空です")
        
        if not user:
            raise ValueError(f"user promptが空です")
        
        self.system_prompt=system
        self.user_prompt=user

        client = OpenAI(
            base_url="http://localhost:11434/v1", # Local Ollama API
            api_key="ollama" # Dummy key
        )

        response = client.chat.completions.create(
            model="gpt-oss:20b", # model: gpt-oss:20b
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": self.user_prompt}
            ]
        )

        # return prompt 
        print(response.choices[0].message.content)
        return (response.choices[0].message.content,)

