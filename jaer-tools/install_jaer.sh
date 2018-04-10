# Needs Java 9
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install default-jre
sudo apt-get install oracle-java9-installer
sudo apt-get install oracle-java9-set-default

# Deps
sudo apt-get install openjfx

# Clone & build JAER
git clone https://github.com/SensorsINI/jaer
cd jaer
ant jar
