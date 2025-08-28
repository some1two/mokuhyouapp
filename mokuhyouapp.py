import os
from google import genai

# Google AI Studioで取得したAPIキーを設定
client = genai.Client(api_key=os.environ.get('yugemipi'))

def chat():
    """チャットの応答を生成するAPIエンドポイント"""
    try:
        user_input = ['user_input']

        # AIチャットのプロンプトを生成
        initial_prompt = f"""
        あなたは、やる気が出ない人に寄り添い、最小単位のタスクを提案する専門家です。
        ユーザーは以下のように話しました。
        「{user_input}」

        ユーザーの言葉から、気分や状況を読み取り、以下の形式で返答してください。

        1. **共感と承認**：まず、ユーザーの気持ちに寄り添う温かい言葉をかけてください。
        2. **具体的なタスクの提案**：次に、ユーザーが今すぐできる、ごく簡単なタスクを1つだけ提案してください。

        ---
        例：
        ユーザー入力：「今日は何もする気が起きないです」
        あなたの返答：「そうですよね、そういう日もありますよね。大丈夫ですよ。
        まずは、窓を開けて深呼吸してみましょうか。」
        """

        # プロンプトをモデルに送信し、応答を取得
        response = client.models.generate_content(model= 'gemini-2.5-flash' , contents = initial_prompt)
        
        # 応答をJSON形式で返す
        print(f"Gemini: {response.text}")

    except Exception as e:
        print(f"エラーが発生しました: {e}")
    

if __name__ == "__main__":
    chat()