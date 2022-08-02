<div align="center">

  # 기업 과제 01 - labq

</div>
<br><br>

## 목차

- [개발 기간](#--개발-기간--)  

- [프로젝트 설명 및 분석](#-프로젝트)

- API 명세서

- [기술 스택](#기술-스택) 
<br><br>

## ⏳ 개발 기간

2022.06.29 ~ 2022.07.01

<br>

## ✍🏻 프로젝트 요구사항

```
Open API를 활용하여 공공데이터 수집 및 가공, 데이터 전달하는 REST API 개발

- Django를 이용하여 REST API 개발
- 서울시 `하수관로 수위 현황`과 `강우량` 정보 json 방식으로 전달받아 데이터 결합
- 결합된 데이터 출력
```



- 서울시 하수관로 수위 현황
  - 요청 인자
    - TYPE : 요청하는 데이터의 타입으로, JSON 타입 데이터를 요청한다.
    - START_INDEX / END_INDEX : 데이터 행의 시작과 끝 번호이다.
    - GUBN : 조회하고자 하는 지역명 코드이다.
- 서울시 강우량 정보
  - 요청인자
    - TYPE : 요청하는 데이터의 타입으로, JSON 타입 데이터를 요청한다.
    - START_INDEX / END_INDEX : 데이터 행의 시작과 끝 번호이다.
    - GU_NAME : 조회하고자 하는 지역명이다.


<br>

## 🍉API 명세서

| METHOD | URI              | 기능                                     |
| ------ | ---------------- | ---------------------------------------- |
| GET    | /rainfall-drain/ | 서울시 하수관로 수위 현황 및 강우량 정보 |

<br>

## 기술 스택

> - Back-End : [![img](https://camo.githubusercontent.com/57ec2ff5dd5ad8c673b06805e02b305b5f13eba756771d734dc370536f12d41e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e20332e31302d3337373641423f7374796c653d666c6174266c6f676f3d507974686f6e266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/57ec2ff5dd5ad8c673b06805e02b305b5f13eba756771d734dc370536f12d41e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e20332e31302d3337373641423f7374796c653d666c6174266c6f676f3d507974686f6e266c6f676f436f6c6f723d7768697465) [![img](https://camo.githubusercontent.com/c408ece01574e98ceb3d78588c62385f17adae7d0fbb69a8707b03132894b478/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f20342e302e342d3039324532303f7374796c653d666c6174266c6f676f3d446a616e676f266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/c408ece01574e98ceb3d78588c62385f17adae7d0fbb69a8707b03132894b478/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f20342e302e342d3039324532303f7374796c653d666c6174266c6f676f3d446a616e676f266c6f676f436f6c6f723d7768697465) [![img](https://camo.githubusercontent.com/79be929c416fe51c5598caeb89f42f1456d6cf19a53dbf3153ab677c0fb9fedb/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f2d44524620332e31332e312d3030393238373f7374796c653d666c6174266c6f676f3d446a616e676f266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/79be929c416fe51c5598caeb89f42f1456d6cf19a53dbf3153ab677c0fb9fedb/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f2d44524620332e31332e312d3030393238373f7374796c653d666c6174266c6f676f3d446a616e676f266c6f676f436f6c6f723d7768697465)
> - ETC　　　: [![img](https://camo.githubusercontent.com/8281207f240f045f9fb74d99fa7ffe64492bbd69501357e192e77978f3352920/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769742d4630353033323f7374796c653d666c61742d6261646765266c6f676f3d476974266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/8281207f240f045f9fb74d99fa7ffe64492bbd69501357e192e77978f3352920/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769742d4630353033323f7374796c653d666c61742d6261646765266c6f676f3d476974266c6f676f436f6c6f723d7768697465) [![img](https://camo.githubusercontent.com/c5282e23e8178a77185cc31077e2e1d45f95b8fec2081a2e31897f32c329cb7e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769746875622d3138313731373f7374796c653d666c61742d6261646765266c6f676f3d476974687562266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/c5282e23e8178a77185cc31077e2e1d45f95b8fec2081a2e31897f32c329cb7e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769746875622d3138313731373f7374796c653d666c61742d6261646765266c6f676f3d476974687562266c6f676f436f6c6f723d7768697465) 
