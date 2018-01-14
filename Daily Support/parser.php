<?php
include_once('simple_html_dom.php');

$url="http://www.dukwon.hs.kr/user/carte/list.do?menuCd=#meals_date";
$html=file_get_html($url);
$josik_ex=$html->find('<ul class="meals_today_list">',0)->children(0);
$jungsik_ex=$html->find('<ul class="meals_today_list">',0)->children(1);
$suksik_ex=$html->find('<ul class="meals_today_list">',0)->children(2);

$josik = explode('ㆍ', $josik_ex);
$str="";
$file=fopen("/home/dukwonlunch/www/data/josik.txt","w+") or die("Unable to open file\n");
for($i=1;$i<count($josik);$i++)
{
    $str=$str.preg_replace("/\s| /",'',$josik[$i])."\n";
}
$str=strip_tags ( $str );
fwrite($file,$str);
fclose($file);

$jungsik = explode('ㆍ', $jungsik_ex);
$str2="";
$file2=fopen("/home/dukwonlunch/www/data/jungsik.txt","w+") or die("Unable to open file\n");
for($i=1;$i<count($jungsik);$i++)
{
    $str2=$str2.preg_replace("/\s| /",'',$jungsik[$i])."\n";
}
$str=strip_tags ( $str2 );
fwrite($file2,$str2);
fclose($file2);

$suksik = explode(' ', $suksik_ex);
$str3="";
$file3=fopen("/home/dukwonlunch/www/data/suksik.txt","w+") or die("Unable to open file\n");
for($i=8;$i<count($suksik);$i++)
{
    $str3=$str3.preg_replace("/\s| /",'',$suksik[$i])."\n";
}
$str3=strip_tags ( $str3 );
fwrite($file3,$str3);
fclose($file3);
?>