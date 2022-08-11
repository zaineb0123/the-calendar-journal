import 'package:flutter/material.dart';
import 'package:apps/constant.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

import 'package:apps/env.dart';
import 'package:apps/models/day.dart';

import '../calendarPage/calendarPage.dart';

class LandingPage extends StatelessWidget {
  const LandingPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    double pageWidth = MediaQuery.of(context).size.width;
    double pageHeight = MediaQuery.of(context).size.height;
    return Container(
        decoration: const BoxDecoration(
            image: DecorationImage(
                image: AssetImage('assets/images/hero-image.jpg'),
                fit: BoxFit.cover)),
        child: Padding(
            padding: const EdgeInsets.all(50),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.end,
              children: <Widget>[
                const Text('BOOST YOUR PRODUCTIVITY',
                    textAlign: TextAlign.justify,
                    style: TextStyle(
                        color: Color.fromARGB(255, 52, 43, 43),
                        fontStyle: FontStyle.italic,
                        fontWeight: FontWeight.w900,
                        fontSize: 24,
                        letterSpacing: 0.5,
                        decoration: TextDecoration.none)),
                const SizedBox(
                  height: 10,
                ),
                const Text('OR',
                    textAlign: TextAlign.justify,
                    style: TextStyle(
                        color: Color.fromARGB(255, 52, 43, 43),
                        fontStyle: FontStyle.italic,
                        fontWeight: FontWeight.w900,
                        fontSize: 24,
                        letterSpacing: 0.5,
                        decoration: TextDecoration.none)),
                const SizedBox(
                  height: 10,
                ),
                const Text('Unwind',
                    textAlign: TextAlign.justify,
                    style: TextStyle(
                        color: Color.fromARGB(255, 52, 43, 43),
                        fontStyle: FontStyle.italic,
                        fontWeight: FontWeight.w900,
                        fontSize: 24,
                        letterSpacing: 0.5,
                        decoration: TextDecoration.none)),
                const SizedBox(
                  height: 20,
                ),
                FittedBox(
                  child: Column(
                    children: <Widget>[
                      const SizedBox(width: 15),
                      ElevatedButton(
                        style: ElevatedButton.styleFrom(
                          // Foreground color
                          onPrimary: Theme.of(context).colorScheme.onPrimary,
                          // Background color
                          primary: Theme.of(context).colorScheme.primary,
                        ).copyWith(elevation: ButtonStyleButton.allOrNull(0.0)),
                        onPressed: () {
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                                builder: (context) => const CalendarPage()),
                          );
                        },
                        child: const Text('Get Started'),
                      ),
                      const SizedBox(width: 15),
                    ],
                  ),
                ),
              ],
            )));
  }
}
