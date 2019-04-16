$docker run -it --rm dharamaraob/omdb:1.0 "jurassic world" </br>
title: Jurassic World </br>
Year: 2015 </br>
Rating: PG-13 </br>
Release Date: 12 Jun 2015 </br>
Show Time: 124 min </br>
Director: Colin Trevorrow </br>
Writer: Rick Jaffa (screenplay by), Amanda Silver (screenplay by), Colin Trevorrow (screenplay by), Derek Connolly (screenplay by), Rick Jaffa (story by), Amanda Silver (story by), Michael Crichton (based on the characters created by) </br>
Rotten Tomatoes Rating: 72% </br>
 </br>
$docker run -it --rm dharamaraob/omdb:1.0 "jurassic park" </br>
title: Jurassic Park </br>
Year: 1993 </br>
Rating: PG-13 </br>
Release Date: 11 Jun 1993 </br>
Show Time: 127 min </br>
Director: Steven Spielberg </br>
Writer: Michael Crichton (novel), Michael Crichton (screenplay), David Koepp (screenplay) </br>
Rotten Tomatoes Rating: 91% </br>
$ docker run -it --entrypoint=/bin/bash dharamaraob/omdb:1.0 </br>
root@1cd31f3338ea:/omdb# python omdb.py --movie i </br>
title: Star Wars: Episode I - The Phantom Menace </br>
Year: 1999 </br>
Rating: PG </br>
Release Date: 19 May 1999 </br>
Show Time: 136 min </br>
Director: George Lucas </br>
Writer: George Lucas </br>
Rotten Tomatoes Rating: 54% </br>

Note: If you are testing the python code, please pass your apikey in config file.

