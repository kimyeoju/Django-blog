# My Blog
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
 - 추후에 추가

## 3. 프로젝트 구조와 개발 일정
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


