# Generated from gemcutter-0.7.0.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	gemcutter

Summary:	Commands to interact with RubyGems.org
Name:		rubygem-%{rbname}

Version:	0.7.1
Release:	3
Group:		Development/Ruby
License:	MIT
URL:		http://rubygems.org
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Adds several commands to RubyGems for managing gems and more on RubyGems.org.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f test

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/gemcutter/version.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rubygems
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rubygems/commands
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rubygems/commands/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.7.1-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Fri Jan 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.7.1-1
+ Revision: 769359
- version update 0.7.1

* Tue Mar 15 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.7.0-1
+ Revision: 645113
- regenerate spec with gem2rpm5
- new version: 0.7.0

* Fri Sep 17 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.6.1-1mdv2011.0
+ Revision: 579222
+ rebuild (emptylog)

* Wed Feb 03 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.3.0-1mdv2011.0
+ Revision: 500540
- add some missing dependencies

* Wed Feb 03 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.3.0-1mdv2010.1
+ Revision: 500361
- import rubygem-gemcutter


* Mon Feb  3 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.3.0-1
- initial release
