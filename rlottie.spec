%global commit0 bfda7feee5dffd298c2b756219586c6c429152f8
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20190705

Name: rlottie
Version: 0
Release: 1.%{date}git%{shortcommit0}%{?dist}

License: LGPLv2.1+
Summary: Platform independent standalone library that plays Lottie Animation

URL: https://github.com/Samsung/%{name}
Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gtest-devel
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: gcc

%description
rlottie is a platform independent standalone C++ library for rendering
vector based animations and art in realtime.

Lottie loads and renders animations and vectors exported in the bodymovin
JSON format. Bodymovin JSON can be created and exported from After Effects
with bodymovin, Sketch with Lottie Sketch Export, and from Haiku.

For the first time, designers can create and ship beautiful animations
without an engineer painstakingly recreating it by hand. Since the animation
is backed by JSON they are extremely small in size but can be large in
complexity!

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{commit0}
sed -e "s/, 'werror=true'//" -e "s/, 'optimization=s'//" -i meson.build

%build
%meson -Dtest=true -Dexample=false -Dmodule=false
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc AUTHORS README.md
%license COPYING
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/%{name}*.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Fri Jul 05 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20190705gitbfda7fe
- Initial SPEC release.
