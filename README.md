# Asym_VDSR
Create lightweight models using Asymmetric_CNN in VDSR
---

# Super-Resolution with fewer parameters by using Asymmetric convolution

[paper](https://github.com/HwangToeMat/Asym_VDSR/raw/master/Multi%20scale%20Super-Resolution%20with%20fewer%20parameters.pdf)

## 연구 주제 

<img src="https://github.com/HwangToeMat/HwangToeMat.github.io/blob/master/AI-Project/image/AsymVDSR/img2.png?raw=true" style="max-width:100%;margin-left: auto; margin-right: auto; display: block;">

**Asymmetric convolution**을 사용하여 기존의 Super-Resolution 모델들의 특징과 성능을 유지하고 **적은 수의 파라미터**로 Super-Resolution 문제를 해결한다.

## 관련 연구

### 1. VDSR

<img src="https://github.com/HwangToeMat/HwangToeMat.github.io/blob/master/AI-Project/image/AsymVDSR/img3.png?raw=true" style="max-width:100%;margin-left: auto; margin-right: auto; display: block;">

* Accurate Image Super-Resolution Using Very Deep Convolutional Networks, Seoul National University, Korea (CVPR 2016)

* 20개의 층으로 이루어진 딥러닝 모델

* residual 값과 skip connection을 지나온 LR을 더해서 SR을 생성

* **실험의 Baseline model로 사용**

### 2. Asymmetric Convolution

<img src="https://github.com/HwangToeMat/HwangToeMat.github.io/blob/master/AI-Project/image/AsymVDSR/img4.png?raw=true" style="max-width:100%;margin-left: auto; margin-right: auto; display: block;">

* kernel이 n\*n의 형태가 아니라 m\*n형태의 비대칭 형태인 convolution 연산

* 그림과 같이 3\*3 크기의 영역을 1\*1로 축소할 때 3\*1, 1\*3 두번의 연산으로 변경 가능(기존의 9개의 파라미터를 6개로 축소)

* 크기가 큰 영역을 축소시킬 수록 더 크게 감소


## 제안 방법 소개

<img src="https://github.com/HwangToeMat/HwangToeMat.github.io/blob/master/AI-Project/image/AsymVDSR/img5.png?raw=true" style="max-width:100%;margin-left: auto; margin-right: auto; display: block;">

기존 VDSR의 구조는 그대로 유지하고 **input, output에 쓰이는 두개의 layer를 제외한 나머지 18개의 layer에 3\*3conv를 3\*1, 1\*3으로 변경**하여 Asym_VDSR 설계
 
## 검증

<img src="https://github.com/HwangToeMat/HwangToeMat.github.io/blob/master/AI-Project/image/AsymVDSR/img1.png?raw=true" style="max-width:100%;margin-left: auto; margin-right: auto; display: block;">

<img src="https://github.com/HwangToeMat/HwangToeMat.github.io/blob/master/AI-Project/image/AsymVDSR/img6.png?raw=true" style="max-width:100%;margin-left: auto; margin-right: auto; display: block;">

* 기존모델과 비교 했을때 Asym_VDSR의 **실행시간이 월등하게 감소**
* PSNR은 기존모델이 약간 높음
* 모델의 **용량 또한 2.68MB -> 1.78MB로 감소**

## 결론 및 추후 연구

### 결론

Asymmetric Convolution을 사용하여 **기존 모델의 구조와 성능은 유지**하면서 연산은 빠르게 할 수 있는 **가벼운 모델로 변경**이 가능했다.

### 추후 연구

1. 하나의 post-upsampling 모델에서 여러가지 Scale의 이미지로 개선할 수 있는 방법을 생각해본다.( 모델의 블록화 실험 진행중 )  
2. Super-Resolution이외의 다른 task(Segmentation, Classification…)에도 Asymmetric Convolution을 적용해 본다.

