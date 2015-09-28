# A program which provides information of noble houses from the HBO series Game of the Thrones.
# Based on the family name provided, this program opens a browser with gameofthrones wikia url.
#
# In console, run the program as below:
#   ruby GoT_noble_houses.rb Lannister
#
# This opens the default browser with url 'http://gameofthrones.wikia.com/wiki/House_Lannister'
module ParseUserInput
  def self.titleize(input_name)
    input_name.split.map(&:capitalize).join
  end
end

module OpenUrl
  # Opens the link based on the house name provided.
  def self.open_url(input_name)
    link = "http://gameofthrones.wikia.com/wiki/House_#{input_name}"
    open_browser(link)
  end

  # Opens the browser from console based on what OS is being used.
  def self.open_browser(link)
    if RbConfig::CONFIG['host_os'] =~ /mswin|mingw|cygwin/
      system "start #{link}"
    elsif RbConfig::CONFIG['host_os'] =~ /darwin/
      system "open #{link}"
    elsif RbConfig::CONFIG['host_os'] =~ /linux|bsd/
      system "xdg-open #{link}"
    end
  end
end

input_name = ParseUserInput::titleize(ARGV[0].to_s)
# Noble houses info credits: http://gameofthrones.wikia.com/wiki/Category:Noble_houses
family_names = [
  'Stark', 'Targaryen', 'Lannister', 'Baratheon', 'Bolton', 'Tyrell', 'Martell', 'Tully', 'Greyjoy', 'Frey', 'Arryn'
]

if (family_names.index(input_name))
  OpenUrl::open_url(input_name)
else
  puts "This program provides information for the following houses only: #{family_names.join(', ')}"
end
