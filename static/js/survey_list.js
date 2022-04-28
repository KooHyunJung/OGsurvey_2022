// 설문지 삭제 alert
function delchk() {
    return confirm("정말 삭제하시겠습니까? 삭제하시면 복구할 수 없습니다");
}

// 설문지 url 복사
function copyToClipboard(val) {
    const t = document.createElement("textarea");
    document.body.appendChild(t);
    t.value = val;
    t.select();
    document.execCommand('copy');
    document.body.removeChild(t);
}

function fn_final(val) {
    var t = 'text'+val
	var url = document.getElementById(t);
	url.style.display='block';	// 숨겨둔 input 태그 block처리
	copyToClipboard(url.value); // url.value copy 함수 연결
	url.style.display='none';	// 다시 숨기기

    alert( url.value + " URL 복사 완료");
    }