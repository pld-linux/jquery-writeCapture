%define		plugin	writeCapture
Summary:	jQuery writeCapture plugin
Name:		jquery-%{plugin}
Version:	1.0.5
Release:	0.1
License:	MIT / GPL
Group:		Applications/WWW
Source0:	https://github.com/iamnoah/writeCapture/tarball/v%{version}/#/%{plugin}-%{version}.tgz
# Source0-md5:	1a7e1cbf56b415c6c2b269bcd4550a1d
URL:		http://iamnoah.github.com/writeCapture/
BuildRequires:	js
BuildRequires:	rpmbuild(macros) > 1.268
BuildRequires:	yuicompressor
Requires:	jquery >= 1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
writeCapture.js is a utility for enabling Ajax in applications with
"legacy" JavaScript (to put it nicely) that can't be gotten rid of.

%prep
%setup -qc
mv *-writeCapture-*/* .

mv plugin/README.md README_plugin.md

%build
install -d build

cat writeCapture.js plugin/jquery.writeCapture.js > build/t.js
yuicompressor --charset UTF-8 build/t.js -o build/jquery.writeCapture.js
js -C -f build/jquery.writeCapture.js

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p build/jquery.writeCapture.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md README_plugin.md
%{_appdir}
