#include "exchange.h"  //exchange.h 설계도를 이 파일로 가져와

// 달러 -> 원화 계산
double won(double usd) { //함수
    return usd * RATE;
}

// 원화 -> 달러 계산
double doll(double krw) {
    return krw / RATE;
}