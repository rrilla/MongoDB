<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<input type="hidden" value=${board.bno }/><br/>
	제목 : <input type="text" value=${board.title } readonly="readonly"/><br/>
	글쓴이 : <input type="text" value=${board.writer } readonly="readonly"/><br/>
	내용 : <textarea rows="5" cols="20" readonly="readonly">${board.content }</textarea>
</body>
</html>