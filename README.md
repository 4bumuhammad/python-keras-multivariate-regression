# Python : Keras using a multivariate regression.

&nbsp;

## &#x1F530; Project

**Explain the purpose :** <br />
Proyek ini akan memprediksi harga rumah berdasarkan beberapa fitur seperti jumlah kamar tidur, luas tanah, dan lainnya. Kita akan menggunakan dataset Boston Housing yang umum digunakan untuk masalah regresi.<br />
Berikut adalah penjelasan singkat tentang masing-masing kolom dalam dataset Boston Housing:<br />

-   CRIM: Per capita crime rate by town.<br />
    Tingkat kejahatan per kapita berdasarkan kota.

-   ZN: Proportion of residential land zoned for lots over 25,000 sq. ft.<br />
    Proporsi tanah perumahan yang dikategorikan untuk lot lebih dari 25.000 kaki persegi.

-   INDUS: Proportion of non-retail business acres per town.<br />
    Proporsi acre bisnis non-ritel per kota.

-   CHAS: Charles River dummy variable (1 if tract bounds river; 0 otherwise).<br />
    Variabel dummy Charles River (1 jika area berbatasan dengan sungai; 0 jika tidak).

-   NOX: Nitric oxide concentration (parts per 10 million).<br />
    Konsentrasi nitrogen oksida (bagian per 10 juta).

-   RM: Average number of rooms per dwelling.<br />
    Jumlah rata-rata kamar per tempat tinggal.

-   AGE: Proportion of owner-occupied units built prior to 1940.<br />
    Proporsi unit yang ditempati pemilik yang dibangun sebelum tahun 1940.

-   DIS: Weighted distances to five Boston employment centers.<br />
    Jarak berbobot ke lima pusat pekerjaan di Boston.

-   RAD: Index of accessibility to radial highways.<br />
    Indeks aksesibilitas ke jalan raya radial.

-   TAX: Full-value property tax rate per $10,000.<br />
    Tingkat pajak properti penuh per $10.000.

-   PTRATIO: Pupil-teacher ratio by town.<br />
    Rasio murid-guru berdasarkan kota.

-   B: 1000(Bk - 0.63)^2 where Bk is the proportion of Black residents by town.<br />
    1000(Bk - 0.63)^2 di mana Bk adalah proporsi penduduk kulit hitam berdasarkan kota.

-   LSTAT: Percentage of lower status of the population.<br />
    Persentase populasi dengan status sosial rendah.

-   MEDV: Median value of owner-occupied homes in $1000s.<br />
    Nilai tengah rumah yang ditempati pemilik dalam ribuan dolar.

&nbsp;

---

&nbsp;

&nbsp;

&nbsp;

## &#x1F530; Begin : 

Creating Directories and File Structures
<pre>
    ❯ pwd
        /Users/.../&lt;project-name&gt;

    ❯ cd &lt;project-name&gt;

    ❯ python -m venv venv

    ❯ source ./venv/bin/activate

    ❯ pip install --no-cache-dir -r requirements.txt




    <!-- ❯ mkdir -p data models utils

    ❯ touch data/__init__.py data/data_loader.py

    ❯ touch models/__init__.py models/prediction_model.py

    ❯ touch utils/__init__.py utils/helper_functions.py

    ❯ touch train.py predict.py -->

    ❯ tree -L 2 -a -I 'README.md|.DS_Store|.git|.gitignore|venv|gambar-petunjuk' ./
        ./
        ├── data
        │   └── boston_housing.csv
        ├── models
        ├── requirements.txt
        └── src
            ├── predict.py
            └── train.py

        3 directories, 4 files
</pre>

&nbsp;

<pre>
    ❯ pip list

        Package                      Version
        ---------------------------- -----------
        absl-py                      2.1.0
        astunparse                   1.6.3
        certifi                      2024.2.2
        charset-normalizer           3.3.2
        flatbuffers                  24.3.25
        gast                         0.5.4
        google-pasta                 0.2.0
        grpcio                       1.64.0
        h5py                         3.11.0
        idna                         3.7
        joblib                       1.4.2
        keras                        3.3.3
        libclang                     18.1.1
        Markdown                     3.6
        markdown-it-py               3.0.0
        MarkupSafe                   2.1.5
        mdurl                        0.1.2
        ml-dtypes                    0.3.2
        namex                        0.0.8
        numpy                        1.26.4
        opt-einsum                   3.3.0
        optree                       0.11.0
        packaging                    24.0
        pandas                       1.3.4
        pip                          22.0.4
        protobuf                     4.25.3
        Pygments                     2.18.0
        python-dateutil              2.9.0.post0
        pytz                         2024.1
        requests                     2.32.1
        rich                         13.7.1
        scikit-learn                 1.4.2
        scipy                        1.13.0
        setuptools                   58.1.0
        six                          1.16.0
        tensorboard                  2.16.2
        tensorboard-data-server      0.7.2
        tensorflow                   2.16.1
        tensorflow-io-gcs-filesystem 0.37.0
        termcolor                    2.4.0
        threadpoolctl                3.5.0
        typing_extensions            4.11.0
        urllib3                      2.2.1
        Werkzeug                     3.0.3
        wheel                        0.43.0
        wrapt                        1.16.0
</pre>

&nbsp;

&nbsp;

&nbsp;

---

&nbsp;

## Run - result

- Train :
<pre>
❯ python3 src/train.py

/Users/.../python-keras-multivariate-regression/venv/lib/python3.10/site-packages/keras/src/layers/core/dense.py:87: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Epoch 1/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 299ms/step - loss: 565.2684
Epoch 1: val_loss improved from inf to 344.13608, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 365ms/step - loss: 565.2684 - val_loss: 344.1361
Epoch 2/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 559.7963
Epoch 2: val_loss improved from 344.13608 to 340.82501, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 559.7963 - val_loss: 340.8250
Epoch 3/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step - loss: 554.4055
Epoch 3: val_loss improved from 340.82501 to 337.51617, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 27ms/step - loss: 554.4055 - val_loss: 337.5162
Epoch 4/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 549.0969
Epoch 4: val_loss improved from 337.51617 to 334.26999, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 27ms/step - loss: 549.0969 - val_loss: 334.2700
Epoch 5/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 543.8885
Epoch 5: val_loss improved from 334.26999 to 331.12808, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 543.8885 - val_loss: 331.1281
Epoch 6/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 538.7805
Epoch 6: val_loss improved from 331.12808 to 328.00226, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 538.7805 - val_loss: 328.0023
Epoch 7/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 533.6967
Epoch 7: val_loss improved from 328.00226 to 324.88504, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 533.6967 - val_loss: 324.8850
Epoch 8/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step - loss: 528.6495
Epoch 8: val_loss improved from 324.88504 to 321.82553, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 27ms/step - loss: 528.6495 - val_loss: 321.8255
Epoch 9/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 523.6692
Epoch 9: val_loss improved from 321.82553 to 318.82489, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 523.6692 - val_loss: 318.8249
Epoch 10/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 518.6978
Epoch 10: val_loss improved from 318.82489 to 315.86978, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 518.6978 - val_loss: 315.8698
Epoch 11/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 513.7086
Epoch 11: val_loss improved from 315.86978 to 312.86493, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 513.7086 - val_loss: 312.8649
Epoch 12/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 508.6716
Epoch 12: val_loss improved from 312.86493 to 309.82077, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 508.6716 - val_loss: 309.8208
Epoch 13/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step - loss: 503.6021
Epoch 13: val_loss improved from 309.82077 to 306.74640, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 503.6021 - val_loss: 306.7464
Epoch 14/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 498.4984
Epoch 14: val_loss improved from 306.74640 to 303.61041, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 498.4984 - val_loss: 303.6104
Epoch 15/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 493.3551
Epoch 15: val_loss improved from 303.61041 to 300.45557, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 493.3551 - val_loss: 300.4556
Epoch 16/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step - loss: 488.1685
Epoch 16: val_loss improved from 300.45557 to 297.26569, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 27ms/step - loss: 488.1685 - val_loss: 297.2657
Epoch 17/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 482.9256
Epoch 17: val_loss improved from 297.26569 to 294.01740, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 482.9256 - val_loss: 294.0174
Epoch 18/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 477.5806
Epoch 18: val_loss improved from 294.01740 to 290.73926, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 477.5806 - val_loss: 290.7393
Epoch 19/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 472.1469
Epoch 19: val_loss improved from 290.73926 to 287.41437, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 472.1469 - val_loss: 287.4144
Epoch 20/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 466.6340
Epoch 20: val_loss improved from 287.41437 to 284.04028, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 466.6340 - val_loss: 284.0403
Epoch 21/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step - loss: 461.0380
Epoch 21: val_loss improved from 284.04028 to 280.62711, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 461.0380 - val_loss: 280.6271
Epoch 22/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 455.3270
Epoch 22: val_loss improved from 280.62711 to 277.17343, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 455.3270 - val_loss: 277.1734
Epoch 23/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 449.5117
Epoch 23: val_loss improved from 277.17343 to 273.66504, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 449.5117 - val_loss: 273.6650
Epoch 24/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 443.6006
Epoch 24: val_loss improved from 273.66504 to 270.09851, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 443.6006 - val_loss: 270.0985
Epoch 25/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 437.5479
Epoch 25: val_loss improved from 270.09851 to 266.47504, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 437.5479 - val_loss: 266.4750
Epoch 26/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 12ms/step - loss: 431.3665
Epoch 26: val_loss improved from 266.47504 to 262.75470, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 29ms/step - loss: 431.3665 - val_loss: 262.7547
Epoch 27/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step - loss: 425.0556
Epoch 27: val_loss improved from 262.75470 to 258.92252, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 29ms/step - loss: 425.0556 - val_loss: 258.9225
Epoch 28/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 418.6212
Epoch 28: val_loss improved from 258.92252 to 255.00818, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 418.6212 - val_loss: 255.0082
Epoch 29/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step - loss: 412.0565
Epoch 29: val_loss improved from 255.00818 to 251.00208, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 412.0565 - val_loss: 251.0021
Epoch 30/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 405.3639
Epoch 30: val_loss improved from 251.00208 to 246.91814, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step - loss: 405.3639 - val_loss: 246.9181
Epoch 31/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 398.5188
Epoch 31: val_loss improved from 246.91814 to 242.78607, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 398.5188 - val_loss: 242.7861
Epoch 32/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 391.5270
Epoch 32: val_loss improved from 242.78607 to 238.57788, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 391.5270 - val_loss: 238.5779
Epoch 33/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 384.3303
Epoch 33: val_loss improved from 238.57788 to 234.29439, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 384.3303 - val_loss: 234.2944
Epoch 34/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 376.9142
Epoch 34: val_loss improved from 234.29439 to 229.94086, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 376.9142 - val_loss: 229.9409
Epoch 35/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 369.3341
Epoch 35: val_loss improved from 229.94086 to 225.53024, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step - loss: 369.3341 - val_loss: 225.5302
Epoch 36/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 361.5729
Epoch 36: val_loss improved from 225.53024 to 221.06235, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 361.5729 - val_loss: 221.0623
Epoch 37/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 353.6271
Epoch 37: val_loss improved from 221.06235 to 216.52563, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step - loss: 353.6271 - val_loss: 216.5256
Epoch 38/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 345.5327
Epoch 38: val_loss improved from 216.52563 to 211.90546, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 345.5327 - val_loss: 211.9055
Epoch 39/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step - loss: 337.3223
Epoch 39: val_loss improved from 211.90546 to 207.22723, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 337.3223 - val_loss: 207.2272
Epoch 40/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 328.9709
Epoch 40: val_loss improved from 207.22723 to 202.43024, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 328.9709 - val_loss: 202.4302
Epoch 41/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step - loss: 320.4648
Epoch 41: val_loss improved from 202.43024 to 197.55579, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 320.4648 - val_loss: 197.5558
Epoch 42/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 311.8184
Epoch 42: val_loss improved from 197.55579 to 192.60538, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 311.8184 - val_loss: 192.6054
Epoch 43/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step - loss: 302.9948
Epoch 43: val_loss improved from 192.60538 to 187.57790, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 302.9948 - val_loss: 187.5779
Epoch 44/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step - loss: 293.9999
Epoch 44: val_loss improved from 187.57790 to 182.50278, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 293.9999 - val_loss: 182.5028
Epoch 45/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step - loss: 284.9040
Epoch 45: val_loss improved from 182.50278 to 177.38110, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 284.9040 - val_loss: 177.3811
Epoch 46/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step - loss: 275.7083
Epoch 46: val_loss improved from 177.38110 to 172.20093, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 27ms/step - loss: 275.7083 - val_loss: 172.2009
Epoch 47/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 266.4347
Epoch 47: val_loss improved from 172.20093 to 166.98764, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 32ms/step - loss: 266.4347 - val_loss: 166.9876
Epoch 48/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 13ms/step - loss: 257.0939
Epoch 48: val_loss improved from 166.98764 to 161.74321, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 32ms/step - loss: 257.0939 - val_loss: 161.7432
Epoch 49/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 247.7052
Epoch 49: val_loss improved from 161.74321 to 156.46590, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 247.7052 - val_loss: 156.4659
Epoch 50/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step - loss: 238.2643
Epoch 50: val_loss improved from 156.46590 to 151.16458, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 27ms/step - loss: 238.2643 - val_loss: 151.1646
Epoch 51/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 12ms/step - loss: 228.7639
Epoch 51: val_loss improved from 151.16458 to 145.82899, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 29ms/step - loss: 228.7639 - val_loss: 145.8290
Epoch 52/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step - loss: 219.2088
Epoch 52: val_loss improved from 145.82899 to 140.46407, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 28ms/step - loss: 219.2088 - val_loss: 140.4641
Epoch 53/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step - loss: 209.6282
Epoch 53: val_loss improved from 140.46407 to 135.09286, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 28ms/step - loss: 209.6282 - val_loss: 135.0929
Epoch 54/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 199.9655
Epoch 54: val_loss improved from 135.09286 to 129.73621, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 199.9655 - val_loss: 129.7362
Epoch 55/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 190.2567
Epoch 55: val_loss improved from 129.73621 to 124.40927, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 190.2567 - val_loss: 124.4093
Epoch 56/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 180.5579
Epoch 56: val_loss improved from 124.40927 to 119.11333, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 27ms/step - loss: 180.5579 - val_loss: 119.1133
Epoch 57/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 170.9422
Epoch 57: val_loss improved from 119.11333 to 113.85882, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 170.9422 - val_loss: 113.8588
Epoch 58/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 161.4235
Epoch 58: val_loss improved from 113.85882 to 108.65675, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 161.4235 - val_loss: 108.6567
Epoch 59/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 152.0125
Epoch 59: val_loss improved from 108.65675 to 103.52086, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 152.0125 - val_loss: 103.5209
Epoch 60/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 142.6914
Epoch 60: val_loss improved from 103.52086 to 98.46709, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 142.6914 - val_loss: 98.4671
Epoch 61/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step - loss: 133.5240
Epoch 61: val_loss improved from 98.46709 to 93.50111, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 27ms/step - loss: 133.5240 - val_loss: 93.5011
Epoch 62/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step - loss: 124.5225
Epoch 62: val_loss improved from 93.50111 to 88.63383, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 124.5225 - val_loss: 88.6338
Epoch 63/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 115.7691
Epoch 63: val_loss improved from 88.63383 to 83.88120, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step - loss: 115.7691 - val_loss: 83.8812
Epoch 64/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 107.2938
Epoch 64: val_loss improved from 83.88120 to 79.25136, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 107.2938 - val_loss: 79.2514
Epoch 65/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 99.1275
Epoch 65: val_loss improved from 79.25136 to 74.74906, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step - loss: 99.1275 - val_loss: 74.7491
Epoch 66/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 91.2940
Epoch 66: val_loss improved from 74.74906 to 70.39680, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step - loss: 91.2940 - val_loss: 70.3968
Epoch 67/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 83.8214
Epoch 67: val_loss improved from 70.39680 to 66.20481, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step - loss: 83.8214 - val_loss: 66.2048
Epoch 68/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 76.7204
Epoch 68: val_loss improved from 66.20481 to 62.18303, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step - loss: 76.7204 - val_loss: 62.1830
Epoch 69/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 70.0224
Epoch 69: val_loss improved from 62.18303 to 58.33952, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step - loss: 70.0224 - val_loss: 58.3395
Epoch 70/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 63.7437
Epoch 70: val_loss improved from 58.33952 to 54.68777, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 63.7437 - val_loss: 54.6878
Epoch 71/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step - loss: 57.9012
Epoch 71: val_loss improved from 54.68777 to 51.23594, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 57.9012 - val_loss: 51.2359
Epoch 72/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 52.5080
Epoch 72: val_loss improved from 51.23594 to 47.98722, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step - loss: 52.5080 - val_loss: 47.9872
Epoch 73/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 47.5694
Epoch 73: val_loss improved from 47.98722 to 44.94873, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step - loss: 47.5694 - val_loss: 44.9487
Epoch 74/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 43.0866
Epoch 74: val_loss improved from 44.94873 to 42.13607, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step - loss: 43.0866 - val_loss: 42.1361
Epoch 75/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 39.0557
Epoch 75: val_loss improved from 42.13607 to 39.55001, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step - loss: 39.0557 - val_loss: 39.5500
Epoch 76/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 35.4742
Epoch 76: val_loss improved from 39.55001 to 37.19139, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 35.4742 - val_loss: 37.1914
Epoch 77/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 32.3332
Epoch 77: val_loss improved from 37.19139 to 35.05347, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 32.3332 - val_loss: 35.0535
Epoch 78/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step - loss: 29.6138
Epoch 78: val_loss improved from 35.05347 to 33.14495, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 29.6138 - val_loss: 33.1450
Epoch 79/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 27.2923
Epoch 79: val_loss improved from 33.14495 to 31.46112, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 27.2923 - val_loss: 31.4611
Epoch 80/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 25.3420
Epoch 80: val_loss improved from 31.46112 to 29.99624, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step - loss: 25.3420 - val_loss: 29.9962
Epoch 81/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 23.7315
Epoch 81: val_loss improved from 29.99624 to 28.74303, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 23.7315 - val_loss: 28.7430
Epoch 82/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 22.4263
Epoch 82: val_loss improved from 28.74303 to 27.69227, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step - loss: 22.4263 - val_loss: 27.6923
Epoch 83/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 21.3888
Epoch 83: val_loss improved from 27.69227 to 26.83468, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step - loss: 21.3888 - val_loss: 26.8347
Epoch 84/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 11ms/step - loss: 20.5804
Epoch 84: val_loss improved from 26.83468 to 26.16063, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 20.5804 - val_loss: 26.1606
Epoch 85/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 19.9633
Epoch 85: val_loss improved from 26.16063 to 25.65188, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 19.9633 - val_loss: 25.6519
Epoch 86/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 19.4989
Epoch 86: val_loss improved from 25.65188 to 25.29232, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step - loss: 19.4989 - val_loss: 25.2923
Epoch 87/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 19.1511
Epoch 87: val_loss improved from 25.29232 to 25.06794, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 19.1511 - val_loss: 25.0679
Epoch 88/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 18.8880
Epoch 88: val_loss improved from 25.06794 to 24.96275, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 26ms/step - loss: 18.8880 - val_loss: 24.9628
Epoch 89/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 18.6837
Epoch 89: val_loss improved from 24.96275 to 24.95940, saving model to /Users/.../python-keras-multivariate-regression/models/multivariate_regression_model.keras
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 25ms/step - loss: 18.6837 - val_loss: 24.9594
Epoch 90/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 18.5070
Epoch 90: val_loss did not improve from 24.95940
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 21ms/step - loss: 18.5070 - val_loss: 25.0413
Epoch 91/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 18.3365
Epoch 91: val_loss did not improve from 24.95940
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 20ms/step - loss: 18.3365 - val_loss: 25.1921
Epoch 92/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 18.1555
Epoch 92: val_loss did not improve from 24.95940
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 20ms/step - loss: 18.1555 - val_loss: 25.3965
Epoch 93/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 17.9519
Epoch 93: val_loss did not improve from 24.95940
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 20ms/step - loss: 17.9519 - val_loss: 25.6367
Epoch 94/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 17.7182
Epoch 94: val_loss did not improve from 24.95940
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 20ms/step - loss: 17.7182 - val_loss: 25.8964
Epoch 95/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 17.4507
Epoch 95: val_loss did not improve from 24.95940
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 20ms/step - loss: 17.4507 - val_loss: 26.1685
Epoch 96/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 17.1491
Epoch 96: val_loss did not improve from 24.95940
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 20ms/step - loss: 17.1491 - val_loss: 26.4439
Epoch 97/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 16.8148
Epoch 97: val_loss did not improve from 24.95940
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 21ms/step - loss: 16.8148 - val_loss: 26.7091
Epoch 98/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 16.4534
Epoch 98: val_loss did not improve from 24.95940
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 20ms/step - loss: 16.4534 - val_loss: 26.9596
Epoch 99/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 16.0704
Epoch 99: val_loss did not improve from 24.95940
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 20ms/step - loss: 16.0704 - val_loss: 27.1896
Epoch 100/100
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 15.6716
Epoch 100: val_loss did not improve from 24.95940
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 20ms/step - loss: 15.6716 - val_loss: 27.3941
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 10ms/step - loss: 34.6546
Test loss: 34.654624938964844
</pre>

&nbsp;

- Predict :

<pre>
    ❯ python3 src/predict.py
    /Users/.../python-keras-multivariate-regression/venv/lib/python3.10/site-packages/keras/src/layers/core/dense.py:87: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
    super().__init__(activity_regularizer=activity_regularizer, **kwargs)
    1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 21ms/step
    [[24.950617 ]
    [23.590525 ]
    [31.386974 ]
    [38.28912  ]
    [37.11076  ]
    [32.654556 ]
    [16.743683 ]
    [18.403463 ]
    [22.516634 ]
    [19.094715 ]
    [18.83973  ]
    [18.324574 ]
    [18.505453 ]
    [13.7580595]
    [12.363728 ]
    [14.266899 ]
    [17.087708 ]
    [14.052711 ]
    [24.202488 ]
    [14.835048 ]
    [21.129202 ]
    [14.994335 ]
    [17.69604  ]
    [17.688997 ]
    [14.793012 ]]
</pre>

&nbsp;

&nbsp;

After : 
<pre>
    ❯ tree -L 2 -a -I 'README.md|.DS_Store|.git|.gitignore|venv|gambar-petunjuk' ./
        ./
        ├── data
        │   └── boston_housing.csv
        ├── models
        │   └── multivariate_regression_model.keras
        ├── requirements.txt
        └── src
            ├── predict.py
            └── train.py

        3 directories, 5 files


    ❯ find ./models -type f -name "*.keras" | sed 's/[^\/]*\//|   /g;s/| *\([^| ]\)/+--- \1/'
        |   +--- multivariate_regression_model.keras    
</pre>

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

---

&nbsp;

<div align="center">
    <img src="./gambar-petunjuk/well_done.png" alt="well_done" style="display: block; margin: 0 auto;">
</div> 

&nbsp;

---

&nbsp;

&nbsp;

&nbsp;