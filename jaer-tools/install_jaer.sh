standard_install()
{
  echo "Standard Install"
  # Clone & build newest JAER
  git clone https://github.com/SensorsINI/jaer
  cd jaer
  ant jar
}

conversion_install()
{
  # Clone & build conversion JAER
  git clone --branch 20170628 https://github.com/SensorsINI/jaer jaer_conversion
  cd jaer_conversion
  ant jar
}

display_help()
{
  echo "[-c] To install conversion jAER"
  echo "[-s] To install standard jAER"
  echo "[-f] To install both stantard and conversion jAER"
}

case $1 in
  -s)
  standard_install
  ;;
  -c)
  echo "Conversion Install"
  conversion_install
  ;;
  -f)
  echo "Full Install"
  standard_install
  conversion_install
  ;;
  --help)
  display_help
  ;;
  *)
  echo "Invalid arguements"
  display_help
  ;;
esac
