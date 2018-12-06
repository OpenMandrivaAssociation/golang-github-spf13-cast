# https://github.com/spf13/cast
%global provider_prefix github.com/spf13/cast
%global gobaseipath     %{provider_prefix}
%global commit          e31f36ffc91a2ba9ddb72a4b6a607ff9b3d3cb63
%global commitdate      20160730

%gocraftmeta -i

Name:           %{goname}
Version:        0
Release:        0.12.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Safe and easy casting from one type to another in Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/spf13/jwalterweatherman)
# Tests deps
BuildRequires: golang(github.com/stretchr/testify/assert)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{gobaseipath} prefix.

%prep
%gosetup

%install
%goinstall

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Tue Feb 27 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.20160730gite31f36f
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gite31f36f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gite31f36f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gite31f36f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 06 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.8.gite31f36f
- Use the standard weather import path prefix
  related: #1413617

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gite31f36f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.6.gite31f36f
- Bump to upstream e31f36ffc91a2ba9ddb72a4b6a607ff9b3d3cb63
  related: #1413617

* Mon Jan 16 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.5.git4d07383
- Polish the spec file
  resolves: #1413617

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git4d07383
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.git4d07383
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git4d07383
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git4d07383
- First package for Fedora
  resolves: #1270063
