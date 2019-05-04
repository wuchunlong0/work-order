
$(function(){
    //编辑器插件
    var sm_toolbar = ['italic','bold', 'underline', 'strikethrough', '|', 'blockquote', 'code', 'link'];
    
    ques.editor = new Simditor({
        textarea: $('#editor'),
        toolbar: sm_toolbar,
        defaultImage : '',//wenda_url+'/home/static/js/plugin/editor/images/image.png',
        pasteImage: false,
        toolbarHidden: false,
        toolbarFloat: false,
        placeholder: '在此回答问题，最多200个字符！要本着“授人以鱼不如授人以渔”的心来回答提问者的问题~。登录才能回答问题。！'
        
    
    });
    //end编辑器插件
})