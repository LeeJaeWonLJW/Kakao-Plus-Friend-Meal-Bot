<?php
$data = json_decode(file_get_contents('php://input'),true);
$content = $data["content"];

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

if ($content == "조식")
{
    $fileopen = fopen("data/josik.txt","r") or die ("Unable file");
    $file = fread($fileopen,filesize("data/josik.txt"));
    $encdata = str_replace("\r\n","\n",$file);
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
    "석식"
            ]
            }
}
EOD;

    fclose($fileopen);
}

else if ($content == "중식")
{
    $fileopen = fopen("data/jungsik.txt","r") or die ("Unable file");
    $file = fread($fileopen,filesize("data/jungsik.txt"));
    $encdata = str_replace("\r\n","\n",$file);
    $encdata = str_replace("</li>","",$file);

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
    "석식"
            ]
            }
}
EOD;

    fclose($fileopen);
}

else if ($content == "석식")
{
    $fileopen = fopen("data/suksik.txt","r") or die ("Unable file");
    $file = fread($fileopen,filesize("data/suksik.txt"));
    $encdata = str_replace("\r\n","\n",$file);
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
    "석식"
            ]
            }
}
EOD;

    fclose($fileopen);
}
?>