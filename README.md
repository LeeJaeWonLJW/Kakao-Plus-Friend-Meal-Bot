# 카카오톡 덕원고등학교 급식 봇 - KakaoTalk Dukwon High School Meal Bot #
<pre>

홈페이지에서 급식을 파싱하여 Linux 스케쥴러를 이용하여 업데이트됩니다.

</pre>

# 사용법 - How to use this Source #
<pre>

/etc/crontab에 아래와 같이 업데이트 스케쥴러를 추가합니다.
시 분    * * *   유저명    php 루트/parser.php

소스와 같은 위치에 data 디렉토리를 생성해줍니다.

Apache2.0 기준으로 VirtualHost를  생성할 때, 아래 두 줄을 추가해주어야합니다.
Options MultiViews
AddType application/x-httpd-php .php

</pre>

# 파일 설명 - Explanation The File #
<pre>
keyboard.php : 초기설정을 담당합니다.
message.php : 저장된 급식 정보를 불러오고, button에 응답합니다.
parser.php : 스케쥴러에 등록하여 매일 급식을 파싱하는 스트립트입니다.
simple_html_dom.php : </pre>[이 소스](http://simplehtmldom.sourceforge.net/)<pre>를 급식 내용을 파싱하기 위해 사용하였습니다.
data 폴더 : 파싱한 급식 정보를 저장해두는 공간입니다.
</pre>

# 사용된 언어 - Usage Language List #

언어(Language) : PHP, HTML</br>
데모(Demo) : [Click](http://dukwon.ga)
