# Generated from gemcutter-0.7.0.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	gemcutter

Summary:	Commands to interact with RubyGems.org
Name:		rubygem-%{rbname}

Version:	0.7.1
Release:	2
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
