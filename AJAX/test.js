// ajax 요청을 보내기 위한 객체 설정
httpRequest = new XMLHttpRequest();

// 응답을 받을 때 호출할 함수 정의
httpRequest.onreadystatechange = function () {
    // Process the server response here
    // First, Needs to check Request's state
    if (httpRequest.readyState === XMLHttpRequest.DONE) {
        // Everything is good, the reponse was received
    } else {
        // not ready yet
    }

    // Second, Check HTTP status codes
    if (httpRequest.status === 200) {
        // perfect!
        // 서버가 보낸 데이터 받아오기
        // 1. String
        httpRequest.responseText()
        // 2. XML
        httpRequest.responseXML()
    } else {
        // have problem with request
        // 404 - Not Found
        // 500 - Internal Server Error
    }
};

// Make Actual Request
// parameters
// 1. HTTP request
// 2. request url
// 3. (optional) Async if true(default): user interact continually
httpRequest.open('GET', 'url', true);
// parameters
// the data you want to send When Post request
// POST data를 원할 때에는 header를 정의하자 (MIME type 지정)
// httpRequest.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
httpRequest.send();
