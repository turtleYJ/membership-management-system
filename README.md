# Membership Management System

## 프로젝트 개요

회원 관리 시스템을 구축합니다. 주요 기능은 사용자 계정 생성, 로그인/로그아웃, 비밀번호 관리, 사용자 정보 수정 등을 포함합니다. ElasticSearch, Redis, NGINX, RabbitMQ, Python, 소켓 프로그래밍을 활용하며, 일부 기능을 마이크로서비스 아키텍처(MSA)로 구현합니다.

## 주요 기능

- **회원 가입 및 로그인**
  - 사용자 계정 생성, 이메일 인증
  - JWT 토큰을 사용한 인증 및 권한 부여
- **사용자 정보 관리**
  - 사용자 정보 조회 및 수정
  - 비밀번호 변경 및 비밀번호 찾기
- **관리자 페이지**
  - 사용자 목록 조회, 사용자 정보 수정
  - 사용자 활동 로그 조회
- **실시간 알림**
  - 소켓 프로그래밍을 통한 실시간 알림 구현
- **마이크로서비스**
  - 인증 서비스, 사용자 관리 서비스, 실시간 알림 서비스로 분리

## 기술 스택

- **Backend**
  - Python: 각 마이크로서비스(API 서버) 구현
  - 데이터 처리 및 RabbitMQ 연동
- **Frontend**
  - React.js: 사용자 인터페이스 구현
- **Database**
  - PostgreSQL, MySQL: 사용자 데이터 저장
  - Redis: 세션 관리 및 캐싱
  - ElasticSearch: 로그 데이터 저장 및 검색
- **DevOps**
  - NGINX: 리버스 프록시 설정 및 서버 관리
- **Real-time Communication**
  - WebSocket: 실시간 데이터 통신
- **Messaging Queue**
  - RabbitMQ: 비동기 작업 처리

## 프로젝트 구조

- **Backend**
  - Python: 주 백엔드 프레임워크로 각 마이크로서비스(API 서버) 구현
  - 데이터 처리 및 RabbitMQ 연동
  - Redis: 세션 관리 및 캐싱
  - RabbitMQ: 비동기 작업 처리
- **Frontend**
  - React.js: 사용자 인터페이스 구현, JWT를 사용한 인증
- **Database**
  - PostgreSQL, MySQL: 사용자 데이터 저장
  - ElasticSearch: 로그 데이터 저장 및 검색
- **Real-time Features**
  - WebSocket: 실시간 알림 및 데이터 업데이트
- **DevOps**
  - NGINX: 리버스 프록시 설정 및 서버 관리

## 설치 및 실행 방법

### 요구 사항

- Docker
- Docker Compose

### 설치

```bash
# 프로젝트를 클론합니다
git clone https://github.com/turtleYJ/membership-management-system.git

# 프로젝트 디렉토리로 이동합니다
cd membership-management-system

# Docker Compose를 사용하여 모든 서비스를 빌드하고 실행합니다
docker-compose up --build
