<!DOCTYPE html>
{% load staticfiles %}
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="">
<meta name="author" content="">
<link rel="icon" href="static/favicon.ico">
<title></title>
<link href="static/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="static/https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">
<link href="static/css/owl.carousel.css" rel="stylesheet">
<link href="static/css/owl.theme.default.min.css" rel="stylesheet">
<link href="static/css/style.css" rel="stylesheet">
<script src="static/js/ie-emulation-modes-warning.js"></script>
<!--[if lt IE 9]>
<script src="static/https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
<script src="static/https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
<![endif]-->
<style>
.userdetails {
    margin-top: -20px;
    margin-left: 30px;
    height: 380px;
    width: 750px;
    overflow: scroll;
}
.userdetails table {
    width: 50em;
    text-align: center;
    border-spacing: 1px;
    background:;
}
.userdetails table tr th {
    background: rgb(0, 128, 128);
    padding: 5px;
}
.userdetails table tr td {
    background: rgba(0, 128, 128, 0.7);
    padding: 5px;
}
.userdetails table tr:hover td {
    background: rgba(0, 128, 128);
}
.sideimage {
    border-style: solid;
    border-width: 1px;
    height: 380px;
    width: 360px;
    margin-top: -380px;
    margin-left: 830px;
    background: url("{% static '16.jpg' %}");
    background-size: 100% 100%;
    float: left;
}
.updatedetails {
    position: absolute;
    margin-top: -40px;
    left: 130px;
    padding: 10px;
    width: 500px;
}
.updatedetails table {
    width: 30em;
    text-align: center;
    background:;
}
.updatedetails table tr th {
    color:;
}
.updatedetails table tr th {
    background: padding: 10px;
}
.updatedetails table tr td {
    background: rgb(0, 128, 128);
    padding: 10px;
}
.updatedetails table tr:hover td {
    background: r);
}
.updateimage {
    border-style: none;
    border-width: 1px;
    height: 350px;
    width: 350px;
    margin-top: -20px;
    margin-left: 740px;
    background: url("{% static '12.png' %}");
    background-size: 100% 100%;
}
</style>
</head>
<body style="background-color:white;">
<nav class="navbar navbar-default navbar-fixed-top">
<div class="container">
<div class="navbar-header page-scroll">
<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
<span class="sr-only">Toggle navigation</span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
</button>
</div>
<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
<ul class="nav navbar-nav navbar-right">
<li class="hidden">
<a href=""></a>
</li>
<li>
<a style="color:WHITE;text-decoration: none;" href="{% url 'admin_page' %}">USER DETAILS</a>
</li>
<li>
<a style="color:WHITE;text-decoration: none;" href="{% url 'admin_networkdata' %}">DATA SET</a>
</li>
<li>
<a style="color:WHITE;text-decoration: none;" href="{% url 'admin_nlpanalysis' %}">OPCODE BAASED MALWARE</a>
</li>
<li>
<a style="color:WHITE;text-decoration: none;" href="{% url 'admin_graphicalanalysis' %}"> GRAPHICAL ANALYSIS</a>
</li>
<li>
<a style="color:WHITE;text-decoration: none;" href="{% url 'admin_algorithms' %}">ACCURACY ANALYSIS</a>
</li>
<li>
<a style="color:WHITE;text-decoration: none;" href="{% url 'view_feedback' %}">VIEW FEEDBACK</a>
</li>
<li>
<a style="color:WHITE;text-decoration: none;" href="{% url 'admin_login' %}"> LOGOUT</a>
</li>
</ul>
</div>
</div>
</nav>
<header>
<div class="container">
<div class="slider-container">
<div class="intro-text">
Robust Malware Detection for Internet Of (Battlefield) Things Devices Using Deep Eigenspace Learning
</div>
</header>
</div>
</div>
<section id="about" class="light-bg">
<div class="userdetails">
<table>
<tr>
<th style="color:white"> FIRST NAME</th>
<th style="color:white">LAST NAME</th>
<th style="color:white">USER ID</th>
<th style="color:white">MOBILE NUMBER</th>
<th style="color:white"><label style="margin-left:60px;">EMAIL</label></th>
<th style="color:white">GENDER</th>
</tr>
{% for i in obje %}
<tr>
<td style="color:white">{{i.firstname}}</td>
<td style="color:white">{{i.lastname}}</td>
<td style="color:white">{{i.userid}}</td>
<td style="color:white">{{i.mblenum}}</td>
<td style="color:white">{{i.email}}</td>
<td style="color:white">{{i.gender}}</td>
</tr>
{% endfor %}
</table>
</div>
<div class="sideimage"></div>
</section>
<section id="about" class="light-bg">
<div class="updatedetails">
<form method="post">
{% csrf_token %}
<table>
<tr>
<td style="color:white">FIRST NAME</td>
<td><input type="text" name="FirstName" value="{{obj.firstname}}"></td>
</tr>
<tr>
<td style="color:white">LAST NAME</td>
<td><input type="text" name="LastName" value="{{obj.lastname}}"></td>
</tr>
<tr>
<td style="color:white">USER ID</td>
<td><input type="text" name="UserId" value="{{obj.userid}}"></td>
<tr>
<tr>
<td style="color:white">PASSWORD</td>
<td><input type="text" name="Password" value="{{obj.password}}"></td>
</tr>
<tr>
<td style="color:white">MOBILE NUMBER</td>
<td><input type="text" name="MobileNumber" value="{{obj.mblenum}}"></td>
</tr>
<tr>
<td style="color:white"> EMAIL ID</td>
<td><input type="text" name="EmailId" value="{{obj.email}}"></td>
</tr>
<tr>
<td style="color:white">GENDER</td>
<td><input type="text" name="Gender" value="{{obj.gender}}"></td>
</tr>
<tr>
<td style="text-align:center;" colspan="2"><input type="submit" name="submit" value="SUBMIT" style="background:red;color:white"></td>
</tr>
</table>
</form>
</div>
<div class="updateimage"></div>
</section>
<footer>
<div class="container text-center">
<marquee style="color:yellow">Robust Malware Detection for Internet Of (Battlefield) Things Devices Using Deep Eigenspace Learning</marquee>
</div>
</footer>
<script src="static/https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script src="static/http://cdnjs.cloudflare.com/ajax/libs/jquery- easing/1.3/jquery.easing.min.js"></script>
<script src="static/js/bootstrap.min.js"></script>
<script src="static/js/owl.carousel.min.js"></script>
<script src="static/js/cbpAnimatedHeader.js"></script>
<script src="static/js/theme-scripts.js"></script>
<script src="static/js/ie10-viewport-bug-workaround.js"></script>
</body>
</html>
