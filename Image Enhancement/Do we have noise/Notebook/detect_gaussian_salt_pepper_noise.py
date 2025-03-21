# coding: utf-8
import cv2
import numpy as np
from scipy.stats import kurtosis, skew
def detect_gaussian_salt_pepper_noise(img):




    # ابتدا انحراف معیار کل تصویر را محاسبه کنید. اگر مقدار انحراف معیار از 20 کمتر بود احتمالا تصویر نویز ندارد



    flatten_img = img.flatten()
    std = np.std(flatten_img)

    if std < 20:
        return "No Noise"




    # بررسی نویز نمک‌فلفل: پیکسل‌های شدید (0 یا 255)

    # برای بررسی نویز فلفل نمک باید تمام پیکسل های تصویر را محاسبه کرد یعنی چند پیکسل دارد تصویر

    total_pixels = len(flatten_img)

    # حال مجموع تعداد پیکسل های با مقادیر 0 یا 255 را با هم محاسبه و جمع میکنیم. یعنی مجموعا چند پیکسل داریم که مقادیر شدت روشنایی انها 0 یا 255 هستند

    extreme_pixels = len(flatten_img[flatten_img == 255]) + len(
        flatten_img[flatten_img == 0]
    )




    # نسبت پیکسل های مقادیر 0 یا 255 به کل پیکسل های تصویر اگر بیشتر از 0.005 باشد احتمالا تصویر نویز فلفل و نمک دارد.

    if extreme_pixels / total_pixels > 0.005:

        return "Salt-and-Pepper"




    # به عنوان تمرین، چگونگی اینکه تصویر نویز گوسی دارد یا خیر را الگوریتمش را شما بنویسید
    skewness = skew(flatten_img)
    kurt = kurtosis(flatten_img, fisher=False)
    if abs(skewness) <= 0.7 and 2.0 <= kurt <= 4.0:
        return "Gaussian"




    # اگر هیچ‌کدام مشخص نشد، فرض می‌کنیم نویز ندارد (برای سادگی)

    return "No Noise"
