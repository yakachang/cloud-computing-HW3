from flask import Flask, jsonify, request
from transformers import QuestionAnsweringPipeline, AutoModelForQuestionAnswering, AutoTokenizer
import torch

app = Flask(__name__)


ctx = '清華大學成立於民國前一年,校址為北平西郊的清華園,最初名稱為「清華學堂」。105年11月1日起,國立清華大學與國立新竹教育大學合併為「國立清華大學」。原「國立新竹教育大學附設實驗國民小學」同時更名為「國立清華大學附設實驗國民小學」。'


def build_pipeline(pretrained_model):
    
    model = AutoModelForQuestionAnswering.from_pretrained(pretrained_model)
    tokenizer = AutoTokenizer.from_pretrained(pretrained_model)
    device_pipeline = 0 if torch.cuda.is_available() else -1
    qa_pipeline = QuestionAnsweringPipeline(model=model,
                                         tokenizer=tokenizer,
                                         device=device_pipeline)

    return qa_pipeline



@app.route("/inference", methods=["GET"])
def inference():
    # data = request.get_json(force=True)

    # print(data)
    # question = data['question']
    question = request.args.get('question', default = '*', type = str)

    res = qa_pipeline({'question': question, 'context': ctx})

    return jsonify(
        {
            "answer": res['answer'],
        }
    )

if __name__ == "__main__":
    pretrained_model = 'wptoux/albert-chinese-large-qa'
    qa_pipeline = build_pipeline(pretrained_model)
    app.run("0.0.0.0", port=8787, debug=False)