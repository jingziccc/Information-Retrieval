from flask import Flask, jsonify, abort, request, make_response, url_for, redirect, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.utils import secure_filename
import os
import shutil
import numpy as np
from search import recommend
import tarfile
from datetime import datetime
from scipy import ndimage

# 允许上传的文件类型
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = 'uploads'
# 创建 Flask 应用
app = Flask(__name__, static_url_path="")
# 上传文件的存储路径
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
auth = HTTPBasicAuth()

# 加载保存的图像特征向量以进行图像检索
extracted_features = np.zeros((2955, 2048), dtype=np.float32)
with open('saved_features_recom.txt') as f:
    for i, line in enumerate(f):
        extracted_features[i, :] = line.split()
print("loaded extracted_features")


# 处理图像上传和检索
@app.route('/imgUpload', methods=['GET', 'POST'])
def upload_img():
    print("image upload")
    result = 'static/result'
    # 如果结果目录不存在则创建
    if not os.path.exists(result):
        os.mkdir(result)
    else:
        shutil.rmtree(result)

    # 判断请求方式是否是 POST
    if request.method == 'POST':
        # 检查是否上传了文件
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)

        file = request.files['file']
        print(file.filename)
        # 如果用户没有选择文件，也就是上传的文件名为空，则返回上传页面
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        # 如果文件存在且文件类型被允许，则进行上传和检索
        if file and file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            inputloc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            # 调用 search.py 中的 recommend 函数进行图像检索
            recommend(inputloc, extracted_features)
            os.remove(inputloc)
            # 返回前端页面所需的图像列表
            image_path = "/result"
            image_list = [os.path.join(image_path, file) for file in os.listdir(result)
                          if not file.startswith('.')]
            images = {}
            for i in range(len(image_list)):  #
                images[f'image{i}'] = image_list[i]

            return jsonify(images)


# 主函数，返回主页
@app.route("/")
def main():
    return render_template("main.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
