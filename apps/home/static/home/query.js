var editor = CodeMirror.fromTextArea(document.getElementById('code_area'), {
    mode: 'text/x-sql',
    theme: 'eclipse', // Bạn có thể thay đổi theme nếu muốn
    lineNumbers: true,
    styleActiveLine: true,
    lineWrapping: true,
});
editor.setSize(null, 600); // Chiều cao 600px