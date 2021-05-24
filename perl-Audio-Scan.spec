#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Audio-Scan
Version  : 1.01
Release  : 20
URL      : https://cpan.metacpan.org/authors/id/A/AG/AGRUNDMA/Audio-Scan-1.01.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AG/AGRUNDMA/Audio-Scan-1.01.tar.gz
Summary  : 'Fast C metadata and tag reader for all common audio file formats'
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-Audio-Scan-license = %{version}-%{release}
Requires: perl-Audio-Scan-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Warn)
BuildRequires : pkgconfig(zlib)
BuildRequires : zlib-dev

%description
NAME
Audio::Scan - Fast C metadata and tag reader for all common audio file
formats

%package dev
Summary: dev components for the perl-Audio-Scan package.
Group: Development
Provides: perl-Audio-Scan-devel = %{version}-%{release}
Requires: perl-Audio-Scan = %{version}-%{release}

%description dev
dev components for the perl-Audio-Scan package.


%package license
Summary: license components for the perl-Audio-Scan package.
Group: Default

%description license
license components for the perl-Audio-Scan package.


%package perl
Summary: perl components for the perl-Audio-Scan package.
Group: Default
Requires: perl-Audio-Scan = %{version}-%{release}

%description perl
perl components for the perl-Audio-Scan package.


%prep
%setup -q -n Audio-Scan-1.01
cd %{_builddir}/Audio-Scan-1.01

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Audio-Scan
cp %{_builddir}/Audio-Scan-1.01/COPYING %{buildroot}/usr/share/package-licenses/perl-Audio-Scan/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Audio::Scan.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Audio-Scan/06877624ea5c77efe3b7e39b0f909eda6e25a4ec

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Audio/Scan.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Audio/Scan/Scan.so
