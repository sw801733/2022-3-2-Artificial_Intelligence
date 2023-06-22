# 2022-3-2-Artificial_Intelligence
3학년 2학기 인공지능 수업



# 과제 1
- C 언어를 활용한 신경망 구현
3 x 3 순전파 (forward propagation) 을 C 언어로 구현

Output의 활성화 함수는 시그모이드 함수 $1/1+e^-x$ 를 사용한다.

시그모이드 함수의 분모에 있는 $e^-x$ 는 x 의 값이 커짐에 따라 작아지므로 
x 값이 커짐에 따라 시그모이드 함수의 결과값은 커지게 된다.

즉, input 의 값은 유지한 상태에서 가중치의 값을 늘려 Layer 에서 계산되는 값들이 커질 경우
Output 의 결과값이 커지는 것을 확인할 수 있었다.






