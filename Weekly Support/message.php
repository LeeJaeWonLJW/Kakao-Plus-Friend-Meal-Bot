<?php
$data = json_decode(file_get_contents('php://input'),true);
$content = $data["content"];
$key = $_GET['key'];

if (!function_exists('codepoint_encode')) {

    function codepoint_encode($str) {
        return substr(json_encode($str), 1, -1);
    }
}
if (!function_exists('codepoint_decode')) {

    function codepoint_decode($str) {
        return json_decode(sprintf('"%s"', $str));
    }
}

if ($content == "조식" or $key==1)
{
    $year=date("Y");
    $month=date("m");
    $day=date("d");

    $hour=date("H");

    if($hour>=8) {
        $fileopen = fopen("data/josik".$year.$month.($day+1).".txt", "r") or die ("Unable file");
        $file = fread($fileopen, filesize("data/josik".$year.$month.($day+1).".txt"));
        $encdata = str_replace("\r\n", "\n", $file);
        $encdata = str_replace("\n\n", "\n", $file);
        $encdata = codepoint_encode($encdata);

        echo <<<EOD
    {
        "message": {
                "text" : "$encdata"},
        "keyboard":{
                "type" : "buttons",
                "buttons":[
                "조식",
                "중식",
                "석식",
				"평가하기"
                ]
                }
    }
EOD;

        fclose($fileopen);
    }

    else
    {
        $fileopen = fopen("data/josik".$year.$month.$day.".txt", "r") or die ("Unable file");
        $file = fread($fileopen, filesize("data/josik".$year.$month.$day.".txt"));
        $encdata = str_replace("\r\n", "\n", $file);
        $encdata = str_replace("\n\n", "\n", $file);
        $encdata = codepoint_encode($encdata);

        echo <<<EOD
    {
        "message": {
                "text" : "$encdata"},
        "keyboard":{
                "type" : "buttons",
                "buttons":[
                "조식",
                "중식",
                "석식",
				"평가하기"
                ]
                }
    }
EOD;

        fclose($fileopen);
    }
}

else if ($content == "중식" or $key==2)
{
    $year=date("Y");
    $month=date("m");
    $day=date("d");

    $hour=date("H");

    if($hour>=13) {
        $fileopen = fopen("data/jungsik".$year.$month.($day+1).".txt", "r") or die ("Unable file");
        $file = fread($fileopen, filesize("data/jungsik".$year.$month.($day+1).".txt"));
        $encdata = str_replace("\r\n", "\n", $file);
        $encdata = str_replace("\n\n", "\n", $file);
        $encdata = codepoint_encode($encdata);

        echo <<<EOD
    {
        "message": {
                "text" : "$encdata"},
        "keyboard":{
                "type" : "buttons",
                "buttons":[
                "조식",
                "중식",
                "석식",
				"평가하기"
                ]
                }
    }
EOD;

        fclose($fileopen);
    }

    else
    {
        $fileopen = fopen("data/jungsik".$year.$month.$day.".txt", "r") or die ("Unable file");
        $file = fread($fileopen, filesize("data/jungsik".$year.$month.$day.".txt"));
        $encdata = str_replace("\r\n", "\n", $file);
        $encdata = str_replace("\n\n", "\n", $file);
        $encdata = codepoint_encode($encdata);

        echo <<<EOD
    {
        "message": {
                "text" : "$encdata"},
        "keyboard":{
                "type" : "buttons",
                "buttons":[
                "조식",
                "중식",
                "석식",
				"평가하기"
                ]
                }
    }
EOD;

        fclose($fileopen);
    }
}

else if ($content == "석식" or $key==3)
{
    $year=date("Y");
    $month=date("m");
    $day=date("d");

    $hour=date("H");

    if($hour>=19) {
        $fileopen = fopen("data/dinner".$year.$month.($day+1).".txt", "r") or die ("Unable file");
        $file = fread($fileopen, filesize("data/dinner".$year.$month.($day+1).".txt"));
        $encdata = str_replace("\r\n", "\n", $file);
        $encdata = str_replace("\n\n", "\n", $file);
        $encdata = codepoint_encode($encdata);

        echo <<<EOD
    {
        "message": {
                "text" : "$encdata"},
        "keyboard":{
                "type" : "buttons",
                "buttons":[
                "조식",
                "중식",
                "석식",
				"평가하기"
                ]
                }
    }
EOD;

        fclose($fileopen);
    }

    else
    {
        $fileopen = fopen("data/dinner".$year.$month.$day.".txt", "r") or die ("Unable file");
        $file = fread($fileopen, filesize("data/dinner".$year.$month.$day.".txt"));
        $encdata = str_replace("\r\n", "\n", $file);
        $encdata = str_replace("\n\n", "\n", $file);
        $encdata = codepoint_encode($encdata);

        echo <<<EOD
    {
        "message": {
                "text" : "$encdata"},
        "keyboard":{
                "type" : "buttons",
                "buttons":[
                "조식",
                "중식",
                "석식",
				"평가하기"
                ]
                }
    }
EOD;

        fclose($fileopen);
    }
}

else if ($content == "평가하기")
{
	echo <<<EOD
    {
		"message": {
		"text" : "아래 보기를 선택하여 조식, 중식, 석식 중 원하는 급식을 평가해주세요. 비속어, 은어 사용하지 말아주세요!선택하면 양식이 나오니 꼭!! 양식을 복사해서 채워주세요."},
        "keyboard":{
                "type" : "buttons",
                "buttons":[
                "조식평가",
                "중식평가",
                "석식평가",
				"돌아가기"
                ]
                }
    }
EOD;
}

else if ($content == "돌아가기")
{
	echo <<<EOD
    {
        "message": {
                "text" : "첫 화면으로 돌아갑니다!!"},
        "keyboard":{
                "type" : "buttons",
                "buttons":[
                "조식",
                "중식",
                "석식",
				"평가하기"
                ]
                }
    }
EOD;
}

else if(strpos($content,"조식평가:") !== false)
{
	$link=mysqli_connect("","","","");
	mysqli_set_charset($link,"utf8");
	$sql="insert into breakfast(breakfast) values('".$content."')";
	$result=mysqli_query($link,$sql);

	mysqli_close($link);


	echo <<<EOD
    {
        "message": {
                "text" : "조식 평가가 저장되었습니다!"},
        "keyboard":{
                "type" : "buttons",
                "buttons":[
                "조식",
                "중식",
                "석식",
				"평가하기"
                ]
                }
    }
EOD;
}

else if(strpos($content,"중식평가:") !== false)
{
    $link=mysqli_connect("","","","");
    mysqli_set_charset($link,"utf8");
    $sql="insert into breakfast(breakfast) values('".$content."')";
    $result=mysqli_query($link,$sql);

    mysqli_close($link);

	echo <<<EOD
    {
        "message": {
                "text" : "중식 평가가 저장되었습니다!"},
        "keyboard":{
                "type" : "buttons",
                "buttons":[
                "조식",
                "중식",
                "석식",
				"평가하기"
                ]
                }
    }
EOD;
}

else if(strpos($content,"석식평가:") !== false)
{
    $link=mysqli_connect("","","","");
    mysqli_set_charset($link,"utf8");
    $sql="insert into breakfast(breakfast) values('".$content."')";
    $result=mysqli_query($link,$sql);

    mysqli_close($link);

	echo <<<EOD
    {
        "message": {
                "text" : "석식 평가가 저장되었습니다!"},
        "keyboard":{
                "type" : "buttons",
                "buttons":[
                "조식",
                "중식",
                "석식",
				"평가하기"
                ]
                }
    }
EOD;
}

else if ($content == "조식평가")
{
	echo <<<EOD
    {
        "message": {
                "text" : "조식평가:"},
        "keyboard":{
                "type" : "text"
                }
    }
EOD;
}

else if ($content == "중식평가")
{
	echo <<<EOD
    {
        "message": {
                "text" : "중식평가:"},
        "keyboard":{
                "type" : "text"
                }
    }
EOD;
}

else if ($content == "석식평가")
{
	echo <<<EOD
    {
        "message": {
                "text" : "석식평가:"},
        "keyboard":{
                "type" : "text"
                }
    }
EOD;
}
?>