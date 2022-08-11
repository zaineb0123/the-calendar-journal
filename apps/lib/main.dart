import 'package:flutter/material.dart';
import 'package:flutter/material.dart';
import './pages/landingPage/landingPage.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'Home',
        theme: ThemeData(
          textTheme: Theme.of(context).textTheme.apply(
              fontFamily: 'Open Sans',
              bodyColor: Colors.white,
              displayColor: Colors.white),
        ),
        home: LandingPage());
  }
}
