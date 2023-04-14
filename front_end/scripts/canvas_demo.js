
var drawing = document.getElementById("drawing")

if (drawing.getContext) { // 确定浏览器支持canvas元素
    var ctx = drawing.getContext("2d")

    ctx.strokeStyle = "red";
    ctx.fillStyle = "#00ff00";
    ctx.fillRect(10, 10, 50, 50); // xywh
    ctx.fillStyle = "rgba(0, 0, 255, 0.5)";
    ctx.fillRect(30, 30, 50, 50); // xywh

    // 取得canvas的图像数据URI
    var imgURI = drawing.toDataURL("image/png");;

    // 显示图像
    var image = document.createElement("img");
    image.src = imgURI;
    document.body.appendChild(image);
}