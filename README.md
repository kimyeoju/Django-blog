# My Blog🧸
 - 나만의 게시글 작성, 사용자들 간의 댓글로 소통하며 소소하게 자신의 일상을 공유하는 일상 블로그

## 1. 목표와 기능
### 1.1 목표
- 회원가입, 로그인, 로그아웃이 구현되어 회원들과 비회원들을 구분할 수 있는 블로그
- 로그인 된 사용자는 자유롭게 게시물을 작성, 수정, 삭제 할 수 있는 블로그
- 게시글의 댓글 작성을 통해 여러 사용자들이 소통할 수 있는 블로그

### 1.2 기능
- 사용자 기능
  - 회원가입, 로그인, 로그아웃
- 게시글 기능
  - 게시글 작성, 조회, 수정, 삭제
  - 조회수 표시
- 댓글 기능
  - 게시글 상세 페이지에 댓글 작성, 조회, 삭제
- 해시태그 기능
  - 게시글 상세 페이지에 해시태그 작성, 조회, 삭제

## 2. 개발 환경 및 배포 URL
### 2.1 개발 환경

 <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">

### 2.2 개발 기간
- 2023년 07월 17일 ~ 2023년 07월 20일

### 2.3 배포 URL
 - http://13.125.17.136:8000/

## 3. 프로젝트 구조와 개발 일정

### 3.1 프로젝트 구조
```
📦 
├─ .gitignore
├─ README.md
└─ projects
   ├─ app
   │  ├─ __init__.py
   │  ├─ asgi.py
   │  ├─ settings.py
   │  ├─ urls.py
   │  ├─ views.py
   │  └─ wsgi.py
   ├─ blog
   │  ├─ __init__.py
   │  ├─ admin.py
   │  ├─ apps.py
   │  ├─ forms.py
   │  ├─ migrations
   │  │  ├─ 0001_initial.py
   │  │  ├─ 0002_post_writer.py
   │  │  ├─ 0003_post_hits.py
   │  │  ├─ 0004_rename_hits_post_hit_post_category.py
   │  │  ├─ 0005_remove_post_category_hashtag_comment.py
   │  │  ├─ 0006_post_category.py
   │  │  ├─ 0007_alter_post_category.py
   │  │  ├─ 0008_remove_post_category.py
   │  │  └─ __init__.py
   │  ├─ models.py
   │  ├─ static
   │  │  ├─ css
   │  │  │  ├─ main.css
   │  │  │  ├─ post.css
   │  │  │  └─ user.css
   │  │  └─ img
   │  │     ├─ comment.png
   │  │     ├─ counter.png
   │  │     ├─ hashtag.png
   │  │     ├─ hashtag2.png
   │  │     ├─ heart.png
   │  │     ├─ index.png
   │  │     ├─ login.png
   │  │     ├─ logout.png
   │  │     ├─ message.png
   │  │     ├─ next.png
   │  │     ├─ people.png
   │  │     ├─ prev.png
   │  │     ├─ time.png
   │  │     ├─ user.png
   │  │     └─ write.png
   │  ├─ templates
   │  │  └─ blog
   │  │     ├─ form_error.html
   │  │     ├─ post_detail.html
   │  │     ├─ post_edit.html
   │  │     ├─ post_form.html
   │  │     ├─ post_list.html
   │  │     └─ post_search.html
   │  ├─ templatetags
   │  │  └─ blog_filter.py
   │  ├─ tests.py
   │  ├─ urls.py
   │  └─ views.py
   ├─ manage.py
   ├─ requirements.txt
   ├─ staticfiles
   │  ├─ admin
   │  │  ├─ css
   │  │  │  ├─ autocomplete.css
   │  │  │  ├─ base.css
   │  │  │  ├─ changelists.css
   │  │  │  ├─ dark_mode.css
   │  │  │  ├─ dashboard.css
   │  │  │  ├─ forms.css
   │  │  │  ├─ login.css
   │  │  │  ├─ nav_sidebar.css
   │  │  │  ├─ responsive.css
   │  │  │  ├─ responsive_rtl.css
   │  │  │  ├─ rtl.css
   │  │  │  ├─ vendor
   │  │  │  │  └─ select2
   │  │  │  │     ├─ LICENSE-SELECT2.md
   │  │  │  │     ├─ select2.css
   │  │  │  │     └─ select2.min.css
   │  │  │  └─ widgets.css
   │  │  ├─ img
   │  │  │  ├─ LICENSE
   │  │  │  ├─ README.txt
   │  │  │  ├─ calendar-icons.svg
   │  │  │  ├─ gis
   │  │  │  │  ├─ move_vertex_off.svg
   │  │  │  │  └─ move_vertex_on.svg
   │  │  │  ├─ icon-addlink.svg
   │  │  │  ├─ icon-alert.svg
   │  │  │  ├─ icon-calendar.svg
   │  │  │  ├─ icon-changelink.svg
   │  │  │  ├─ icon-clock.svg
   │  │  │  ├─ icon-deletelink.svg
   │  │  │  ├─ icon-no.svg
   │  │  │  ├─ icon-unknown-alt.svg
   │  │  │  ├─ icon-unknown.svg
   │  │  │  ├─ icon-viewlink.svg
   │  │  │  ├─ icon-yes.svg
   │  │  │  ├─ inline-delete.svg
   │  │  │  ├─ search.svg
   │  │  │  ├─ selector-icons.svg
   │  │  │  ├─ sorting-icons.svg
   │  │  │  ├─ tooltag-add.svg
   │  │  │  └─ tooltag-arrowright.svg
   │  │  └─ js
   │  │     ├─ SelectBox.js
   │  │     ├─ SelectFilter2.js
   │  │     ├─ actions.js
   │  │     ├─ admin
   │  │     │  ├─ DateTimeShortcuts.js
   │  │     │  └─ RelatedObjectLookups.js
   │  │     ├─ autocomplete.js
   │  │     ├─ calendar.js
   │  │     ├─ cancel.js
   │  │     ├─ change_form.js
   │  │     ├─ collapse.js
   │  │     ├─ core.js
   │  │     ├─ filters.js
   │  │     ├─ inlines.js
   │  │     ├─ jquery.init.js
   │  │     ├─ nav_sidebar.js
   │  │     ├─ popup_response.js
   │  │     ├─ prepopulate.js
   │  │     ├─ prepopulate_init.js
   │  │     ├─ theme.js
   │  │     ├─ urlify.js
   │  │     └─ vendor
   │  │        ├─ jquery
   │  │        │  ├─ LICENSE.txt
   │  │        │  ├─ jquery.js
   │  │        │  └─ jquery.min.js
   │  │        ├─ select2
   │  │        │  ├─ LICENSE.md
   │  │        │  ├─ i18n
   │  │        │  │  ├─ af.js
   │  │        │  │  ├─ ar.js
   │  │        │  │  ├─ az.js
   │  │        │  │  ├─ bg.js
   │  │        │  │  ├─ bn.js
   │  │        │  │  ├─ bs.js
   │  │        │  │  ├─ ca.js
   │  │        │  │  ├─ cs.js
   │  │        │  │  ├─ da.js
   │  │        │  │  ├─ de.js
   │  │        │  │  ├─ dsb.js
   │  │        │  │  ├─ el.js
   │  │        │  │  ├─ en.js
   │  │        │  │  ├─ es.js
   │  │        │  │  ├─ et.js
   │  │        │  │  ├─ eu.js
   │  │        │  │  ├─ fa.js
   │  │        │  │  ├─ fi.js
   │  │        │  │  ├─ fr.js
   │  │        │  │  ├─ gl.js
   │  │        │  │  ├─ he.js
   │  │        │  │  ├─ hi.js
   │  │        │  │  ├─ hr.js
   │  │        │  │  ├─ hsb.js
   │  │        │  │  ├─ hu.js
   │  │        │  │  ├─ hy.js
   │  │        │  │  ├─ id.js
   │  │        │  │  ├─ is.js
   │  │        │  │  ├─ it.js
   │  │        │  │  ├─ ja.js
   │  │        │  │  ├─ ka.js
   │  │        │  │  ├─ km.js
   │  │        │  │  ├─ ko.js
   │  │        │  │  ├─ lt.js
   │  │        │  │  ├─ lv.js
   │  │        │  │  ├─ mk.js
   │  │        │  │  ├─ ms.js
   │  │        │  │  ├─ nb.js
   │  │        │  │  ├─ ne.js
   │  │        │  │  ├─ nl.js
   │  │        │  │  ├─ pl.js
   │  │        │  │  ├─ ps.js
   │  │        │  │  ├─ pt-BR.js
   │  │        │  │  ├─ pt.js
   │  │        │  │  ├─ ro.js
   │  │        │  │  ├─ ru.js
   │  │        │  │  ├─ sk.js
   │  │        │  │  ├─ sl.js
   │  │        │  │  ├─ sq.js
   │  │        │  │  ├─ sr-Cyrl.js
   │  │        │  │  ├─ sr.js
   │  │        │  │  ├─ sv.js
   │  │        │  │  ├─ th.js
   │  │        │  │  ├─ tk.js
   │  │        │  │  ├─ tr.js
   │  │        │  │  ├─ uk.js
   │  │        │  │  ├─ vi.js
   │  │        │  │  ├─ zh-CN.js
   │  │        │  │  └─ zh-TW.js
   │  │        │  ├─ select2.full.js
   │  │        │  └─ select2.full.min.js
   │  │        └─ xregexp
   │  │           ├─ LICENSE.txt
   │  │           ├─ xregexp.js
   │  │           └─ xregexp.min.js
   │  ├─ css
   │  │  ├─ main.css
   │  │  ├─ post.css
   │  │  └─ user.css
   │  └─ img
   │     ├─ comment.png
   │     ├─ counter.png
   │     ├─ hashtag.png
   │     ├─ hashtag2.png
   │     ├─ heart.png
   │     ├─ index.png
   │     ├─ login.png
   │     ├─ logout.png
   │     ├─ message.png
   │     ├─ people.png
   │     ├─ time.png
   │     ├─ user.png
   │     └─ write.png
   ├─ templates
   │  ├─ base.html
   │  ├─ index.html
   │  └─ navbar.html
   └─ users
      ├─ __init__.py
      ├─ admin.py
      ├─ apps.py
      ├─ forms.py
      ├─ migrations
      │  ├─ 0001_initial.py
      │  └─ __init__.py
      ├─ models.py
      ├─ templates
      │  └─ user
      │     ├─ user_login.html
      │     └─ user_register.html
      ├─ tests.py
      ├─ urls.py
      └─ views.py
```

### 3.2 개발 일정

- 2023년 07월 17일
  - 메인 페이지 구현
   - 메인, 게시글 url 설정
  - 게시글 모델 생성
   - 게시글 작성, 수정, 삭제, 이동, 게시글 목록, 상세보기 기능 구현

- 2023년 07월 18일
  - 사용자 모델 생성
   - 회원가입, 로그인, 로그아웃 기능 구현
  - 게시글 관련 기능의 사용자 인증
   - 로그인 된 회원만 게시글 작성, 삭제, 수정 기능 구현
  - 게시글 관련 검색
   - 상세보기 게시글 안의 해시태그 검색 기능 구현

- 2023년 07월 19일
  - 댓글 모델 생성
   - 상세보기 게시글의 댓글 작성, 삭제기능 구현
  - 해시태그 모델 생성
   - 상세보기 게시글의 해시태그 작성기능 구현
  - UI 일부 적용
   - 상단바, 햄버거 구현
   - 게시글 목록, 로그인 페이지 템플릿 구현

- 2023년 07월 20일
  - 게시글 목록
   - 게시글 목록의 조회수 기능 구현
   - 한 페이지 당 10개의 글로 제한하는 페이징 처리기능 구현
   - 작성한 순서대로 게시글 번호 표기
   - 게시글 목록 제목에 댓글 개수 표기
  - UI 일부 적용
   - 게시글 상세보기 댓글, 해시태그 UI 적용
  - 정적 파일 모으기
   - python manage.py collectstatic 명령어를 통해 staticfiles 폴더에 css, img 파일 모음

## 4. 상세 페이지 설명

### 메인 페이지

(로그인 전)메인 페이지

![로그인 전 메인페이지](https://github.com/kimyeoju/Django-blog/assets/131739526/cc507e97-c3a6-43d8-917a-1c5a38f3847d)

  - 사용자가 로그인하지 않았을 경우, 상단바에 로그인과 회원가입 버튼이 보임

 (로그인 후)메인 페이지

![로그인 후 메인페이지](https://github.com/kimyeoju/Django-blog/assets/131739526/9607da40-07ba-4817-acb4-6188d455966b)

   - 사용자가 로그인했을 경우, 상단바에 글작성, 로그아웃 버튼이 보임

### 회원가입 페이지

![회원가입페이지](https://github.com/kimyeoju/Django-blog/assets/131739526/aa71df60-64b8-4db5-b369-73371e9717f0)

 - Django에서 제공하는 UserCreationForm을 사용

### 로그인 페이지

![회원가입](https://github.com/kimyeoju/Django-blog/assets/131739526/139cac7f-d9aa-4974-813b-239b49e47963)


### 게시글 목록

(로그인 전)게시글 목록

![게시판 목록 로그인 x](https://github.com/kimyeoju/Django-blog/assets/131739526/ca43f90e-dc5c-4412-89b6-9b741e45fa73)

(로그인 후)게시글 목록

![게시판 목록 로그인 o](https://github.com/kimyeoju/Django-blog/assets/131739526/e37dc800-0285-46da-8db8-40561158675f)


 - 게시글 목록에서 해당 게시물을 클릭하면 게시물의 상세 내용을 확인할 수 있음
 - 게시글 제목 옆에 댓글의 개수가 몇 개인지 확인할 수 있다.
 - 사용자가 상세 게시글에 접근할 때마다 조회수가 올라간다.

### 게시글 상세 페이지

(자신이 작성한) 게시글

![상세페이지 로그인후](https://github.com/kimyeoju/Django-blog/assets/131739526/832dfdb8-7692-417a-b72a-9cb880c4741f)

   - 자신이 작성한 게시글만 수정, 삭제 버튼이 보임

(자신이 작성하지않은) 게시글

![상세페이지 로그인 후 ](https://github.com/kimyeoju/Django-blog/assets/131739526/653c4301-48a0-403b-a759-39f400169d59)

   - 자신이 작성한 댓글만 등록, 삭제 버튼이 보임

### 게시글 작성, 수정 페이지

<img width="1440" alt="스크린샷 2023-07-21 오전 2 47 35" src="https://github.com/kimyeoju/Django-blog/assets/131739526/4df1ea58-b574-41ca-ad82-5122c6c96b3e">


 - 사용자는 게시글을 작성할 수 있으며, 기존의 작성했던 게시글의 내용을 불러와 수정할 수 있다.
 - 수정이 완료된 후에는 해당 게시글의 상세페이지로 돌아가 수정된 글을 확인할 수 있다.


### 상세페이지 안의 태그 검색

![chrome-capture-2023-6-21](https://github.com/kimyeoju/Django-blog/assets/131739526/3bbc4601-3d6d-4f48-9fe8-c630b4ce8bae)

# 5. 실행 화면

### 로그인 기능

![chrome-capture-2023-6-21 (2)](https://github.com/kimyeoju/Django-blog/assets/131739526/9e5c1df1-9c10-45c7-bd2a-98d0ae658649)

### 회원가입 기능

![chrome-capture-2023-6-21 (2)](https://github.com/kimyeoju/Django-blog/assets/131739526/58851291-5040-4421-bceb-217ab5ef225a)

 - 회원가입이 성공적으로 완료가 된다면 로그인 페이지로 돌아간다.

### 게시글, 댓글, 해시태그 작성, 삭제 기능

![chrome-capture-2023-6-21 (4)](https://github.com/kimyeoju/Django-blog/assets/131739526/3177b14b-8454-49d9-98a7-92916699b196)




# 6. 느낀점 및 추후 계획

### 느낀점
  - Django 강의를 들으면서 생소한 환경세팅부터 몇번을 봐도 이해가 가지않는 코드가 많았다. 프로젝트 시작 전에는 과연 내가 기능 하나를 제대로 구현할 수 있을까 하는 막연한 두려움이 있었다. 하지만 프로젝트가 시작하고 나서 혼자 기능을 구현하며 오류를 수정하고 시행착오를 겪는 과정에서 장고의 원리와 구조를 깊게 이해하는 시간이 되었다.
  - Django에서 제공하는 문서를 정독하며 장고에 대한 기능을 추가로 알게 되었고, DB에서 객체를 가져오는 것에 서툴렀는데 DB에서 객체를 가져오는 것 또한 프로젝트를 진행하면서 점차 익숙해진 시간이 되었다.
  - 또한 프로젝트 진행 전에는 장고가 익숙치 않아 막연하고 무서웠다면 프로젝트를 진행하고 나서는 매뉴얼에 따르면 간편한 코드로 쉽고 빠르게 완성할 수 있다는 장고의 장점을 확실히 느끼게 되는 시간이었다. 

### 아쉬웠던점
  - UI와 검색 기능 동작 구현으로 HTML, JS를 사용하면서 계획했던 UI를 제시간 안에 제대로 구현할 수 없었다. 이를 통해 HTML과 JS도 아직 많이 부족하구나 라는 것을 깨닫고 적어도 계획했던 위치에는 빠르게 할 수 있도록 공부를 해야겠다는 생각이 들었다.

### 개선점
  - 장고에 대한 이해도는 전보다 높아졌으나, 고도화를 하기엔 코드의 이해도가 많이 부족하기 때문에 코드를 더 깊게 공부할 것
  - 페이징처리에는 성공했으나, 게시글 목록에 번호를 할당하는 것에 실패했다. 추후에 템플릿 필터 함수에 대한 장고 추가 외부 라이브러리 기능의 이해도를 높여야 한다고 느낌

### 추가해야 할 추후 기능
  - 사용자 관련 추가 기능
   - 비밀번호 변경 기능, 프로필 수정, 닉네임 추가
  - 게시글 관련 추가 기능
    - 게시글 사진 업로드, 카테고리 추가, 좋아요 추가
  - 댓글 추가 기능
   - 대댓글
  
  










