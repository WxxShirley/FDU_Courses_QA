import 'package:flutter/material.dart';
import 'package:bubble/bubble.dart';


void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: '旦课答',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget
{
  @override
  MyHomePage({Key key}):super(key: key);
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage>
{
  @override
   Widget build(BuildContext context)
   {
      double pixelRatio = MediaQuery.of(context).devicePixelRatio;
      double px = 1/pixelRatio;

      BubbleStyle styleSomebody = BubbleStyle(
        nip: BubbleNip.leftTop,
        color: Colors.white,
        elevation: 1*px,
        margin: BubbleEdges.only(top: 8.0,right:50.0),
        alignment: Alignment.topLeft,
      );
      BubbleStyle styleMe = BubbleStyle(
        nip: BubbleNip.rightTop,
        color: Color.fromARGB(255,255,255,199),
        elevation:1*px,
        margin: BubbleEdges.only(top:8.0, left:50.0),
        alignment:Alignment.topRight,
      );

       return Scaffold(
          appBar: AppBar(
            title: Text("旦课答"),
          ),
          body: Container(
            color: Colors.yellow.withAlpha(64),
            child: ListView(
              padding: EdgeInsets.all(8.0),
              children: <Widget>[
                Bubble(
                  alignment: Alignment.center,
                  color: Color.fromARGB(255, 212, 234, 244),
                  elevation: 1*px,
                  margin: BubbleEdges.only(top: 8.0),
                  child: Text('TODAY',style: TextStyle(fontSize:12)),
                  ),
                  Container(height:20, ),
                Bubble(
                  style: styleMe,
                  child: Text('模式识别与机器学习给分怎么样',style: TextStyle(fontSize:12)),
                ),
                Container(height:20,),
                Bubble(
                  style: styleSomebody,
                  child: Text('模式识别与机器学习评价情况为邱博的课，内容很硬核，能学到很多机器学习、深度学习的内容~',style: TextStyle(fontSize:12)),
                ),
                Container( height:20, ),
                Bubble(
                  style: styleMe,
                  child: Text('中文系开设的七大模块课程有哪些',style: TextStyle(fontSize:12)),
                ),
                Container(height:20, ),
                Bubble(
                  style: styleSomebody,
                  child: Text('中文系开设的七大模块类型的课程有中国现代散文导读、古典诗词导读、中国当代小说选读等～',style: TextStyle(fontSize:12)),
                ),
                Container( height:20,),
                Bubble(
                  style: styleMe,
                  child: Text("陶晓鹏老师上哪些课",style: TextStyle(fontSize:12)),
                ),
                Container( height:20, ),
                Bubble(
                  style: styleSomebody,
                  child: Text('陶晓鹏教授的课程有：从计算到智能、信息论与编码~',style: TextStyle(fontSize:12))
                ),
                Container(height:20),
                Bubble(
                  style: styleMe,
                  child: Text('计算机科学技术学院开设的评价不错的专业选修课程有哪些?',style: TextStyle(fontSize:12)),
                ),
                Container(height:20),
                Bubble(
                  style: styleSomebody,
                  child: Text('计算机科学技术学院开设的评价不错的专业选修课程有：分布式系统、虚拟现实引论、模式识别与机器学习等～',style: TextStyle(fontSize:12))
                )
              ],
            ),
          )
       );

   }
}

