#
# TODO:
#	- product registration mechanism (like installzopeproduct script for Zope 2)
#
Summary:	An application server and portal toolkit for building Web sites
Summary(es):	Un servidor de aplicaciones y un conjunto de herramientas para la construcción de sitios Web
Summary(pl):	Serwer aplikacji i toolkit portalowy do tworzenia serwisów WWW
Summary(pt_BR):	Um servidor de aplicações e um conjunto de ferramentas para construção de sites Web
Name:		Zope3
Version:	3.1.0
%define		sub_ver c1
Release:	0.%{sub_ver}.0.1
License:	Zope Public License (ZPL)
Group:		Networking/Daemons
Source0:	http://www.zope.org/Products/Zope3/%{version}%{sub_ver}/%{name}-%{version}%{sub_ver}.tgz
# Source0-md5:	e22eeeae5de89c0eea9edabe3f2c3c4d
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	%{name}.logrotate
Source4:	mkzope3instance
URL:		http://dev.zope.org/Zope3
BuildRequires:	python-devel >= 1:2.4.1
BuildRequires:	perl-base
BuildRequires:	rpmbuild(macros) >= 1.213
PreReq:		rc-scripts
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(post,preun):	/sbin/chkconfig
Requires:	expat >= 1.95.7
Requires:	logrotate
Requires:	python >= 2.4.1
Requires:	python-modules >= 2.4.1
Requires:	python-libs >= 2.4.1
Requires:	python-zope = %{epoch}:%{version}-%{release}
%pyrequires_eq	python
Provides:	group(zope)
Provides:	user(zope)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		zope_dir /usr/lib/zope3

%description
The Z Object Programming Environment (Zope) is a free, Open Source
Python-based application server for building high-performance, dynamic
web sites, using a powerful and simple scripting object model and
high-performance, integrated object database.

This project is a redesign of Zope 2 and seeks to improve the Zope development
experience through the use of Interfaces and Components.

%description -l es
Zope es una aplicación basada en Python, Open Source[tm], para la
construcción de sitios dinámicos, usa un modelo de escritura de
guiones poderoso y sencillo. Para instalar la aplicación Zope, instale
ese paquete y después, Zope-server, para un servidor HTTP integrado
simple, Zope-pcgi, para uso con el servidor Apache. Si desea instalar
solamente algunas partes de la aplicación Zope, están diponibles otros
subpaquetes, usted debe instalar éstos en vez de ese RPM.

%description -l pl
Zope (Z Object Programming Environment - Obiektowe ¦rodowisko
Programistyczne Z) jest opartym o Pythona serwerem aplikacji do
tworzenia wysoko wydajnych, dynamicznych serwisów WWW, przy u¿yciu
u¿ytecznego i prostego modelu obiektowego skryptów oraz wysoko
wydajnej zintegrowanej obiektowej bazy danych.

%description -l pt_BR
Zope é uma aplicação baseada em Python, Open Source[tm], para
construção de sites dinâmicos, usando um modelo de scripting poderoso
e simples Para instalar o Zope, instale esse pacote e depois, ou o
Zope-server, para um servidor HTTP integrado simples, ou Zope-pcgi,
para uso com o Apache. Se você quiser instalar apenas algumas partes
do Zope, outros sub-pacotes estão disponíveis, e você deveria instalar
eles ao invés desse RPM.

%package -n python-zope
Summary:	Python packages developed as part of the Zope 3 project
Summary(pl):	Modu³y Pythona rozwijane w projekcie Zope 3
Group:		Development/Tools
Provides:	ZopeInterface
Provides:	python-zope-cachedescriptors = %{epoch}:%{version}-%{release}
Provides:	python-zope-component = %{epoch}:%{version}-%{release}
Provides:	python-zope-configuration = %{epoch}:%{version}-%{release}
Provides:	python-zope-deprecation = %{epoch}:%{version}-%{release}
Provides:	python-zope-documenttemplate = %{epoch}:%{version}-%{release}
Provides:	python-zope-event = %{epoch}:%{version}-%{release}
Provides:	python-zope-exceptions = %{epoch}:%{version}-%{release}
Provides:	python-zope-hookable = %{epoch}:%{version}-%{release}
Provides:	python-zope-i18n = %{epoch}:%{version}-%{release}
Provides:	python-zope-i18nmessageid = %{epoch}:%{version}-%{release}
Provides:	python-zope-index = %{epoch}:%{version}-%{release}
Provides:	python-zope-interface = %{epoch}:%{version}-%{release}
Provides:	python-zope-modulealias = %{epoch}:%{version}-%{release}
Provides:	python-zope-pagetemplate = %{epoch}:%{version}-%{release}
Provides:	python-zope-proxy = %{epoch}:%{version}-%{release}
Provides:	python-zope-publisher = %{epoch}:%{version}-%{release}
Provides:	python-zope-schema = %{epoch}:%{version}-%{release}
Provides:	python-zope-security = %{epoch}:%{version}-%{release}
Provides:	python-zope-server = %{epoch}:%{version}-%{release}
Provides:	python-zope-structuredtext = %{epoch}:%{version}-%{release}
Provides:	python-zope-tal = %{epoch}:%{version}-%{release}
Provides:	python-zope-tales = %{epoch}:%{version}-%{release}
Provides:	python-zope-testing = %{epoch}:%{version}-%{release}
Provides:	python-zope-thread = %{epoch}:%{version}-%{release}
Obsoletes:	ZopeInterface

%description -n python-zope
The "zope" package is a pure namespace package holding packages
developed as part of the Zope 3 project.

Generally, the immediate subpackages of the "zope" package should be
useful and usable outside of the Zope application server. Subpackages
of the "zope" package should have minimal interdependencies, although
most depend on "zope.interface".

%description -n python-zope -l pl
Pakiet "zope" to pakiet czystej przestrzeni nazw przechowuj±cej
pakiety tworzone jako czê¶æ projektu Zope 3.

Ogólnie bezpo¶rednie podpakiety pakietu "zope" powinny byæ przydatne i
u¿ywalne poza serwerem aplikacji Zope. Podpakiety pakietu "zope"
powinny mieæ minimalne zale¿no¶ci wzajemne, chocia¿ wiêkszo¶æ zale¿y
od "zope.interface".

%prep
%setup -q -n Zope-%{version}%{sub_ver}
cp %{SOURCE4} ./mkzope3instance
chmod a+x ./mkzope3instance

%build
./configure \
	--prefix=%{zope_dir} \
	--force
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_sbindir}} \
	$RPM_BUILD_ROOT{/etc/logrotate.d,/etc/sysconfig,/etc/rc.d/init.d} \
	$RPM_BUILD_ROOT{/var/lib/zope3/main,/var/run/zope3,/var/log/zope3/main} \
	$RPM_BUILD_ROOT%{_sysconfdir}/zope3/main
	
python install.py -q install --skip-build --home "%{zope_dir}" --root "$RPM_BUILD_ROOT"
mv $RPM_BUILD_ROOT%{zope_dir}/lib/python/zope  $RPM_BUILD_ROOT%{py_sitedir}

cat >$RPM_BUILD_ROOT%{zope_dir}/bin/mkzopeinstance <<EOF
#!/usr/bin/python
import sys
from zope.app.server.mkzopeinstance import main
sys.exit(main(from_checkout=False))
EOF

PYTHONPATH="$RPM_BUILD_ROOT%{py_sitedir}/zope:$RPM_BUILD_ROOT%{zope_dir}/lib/python" \
	DESTDIR="$RPM_BUILD_ROOT" sh -x ./mkzope3instance main -u zope:zope

cat >> $RPM_BUILD_ROOT%{py_sitedir}/zope/app/__init__.py <<EOF
import sys
sys.path.insert(0,"%{zope_dir}/lib/python")
EOF

%py_comp $RPM_BUILD_ROOT%{py_sitedir}/zope
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/zope
%py_postclean

rm $RPM_BUILD_ROOT%{zope_dir}/zopeskel/bin/{*.bat.in,zopeservice*}

for f in zconfig zconfig_schema2html zopetest; do
	ln -sf %{zope_dir}/bin/"$f" $RPM_BUILD_ROOT%{_sbindir}/"$f"
done
for f in mkzeoinst runzeo zdctl zdrun zeoctl zeopasswd ; do
	ln -sf %{zope_dir}/bin/"$f".py $RPM_BUILD_ROOT%{_sbindir}/"$f"
done

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/zope3
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/zope3
install %{SOURCE3} $RPM_BUILD_ROOT/etc/logrotate.d/zope3
install %{SOURCE4} $RPM_BUILD_ROOT%{_sbindir}/mkzope3instance

touch $RPM_BUILD_ROOT/var/log/zope3/main/access.log
touch $RPM_BUILD_ROOT/var/log/zope3/main/transcript.log
touch $RPM_BUILD_ROOT/var/log/zope3/main/z3.log

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 112 zope
%useradd -u 112 -d /var/lib/zope/main -s /bin/false -c "Zope User" -g zope zope

%post
/sbin/chkconfig --add zope3
if [ -f /var/lock/subsys/zope3-main ]; then
	/etc/rc.d/init.d/zope3 restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/zopew start\" to start Zope 3 daemon."
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/zope3 ]; then
		/etc/rc.d/init.d/zope3 stop
	fi
	/sbin/chkconfig --del zope3
fi

%postun
if [ "$1" = "0" ] ; then
	%userremove zope
	%groupremove zope
fi

%files
%defattr(644,root,root,755)
%doc Zope/doc/*
%attr(754,root,root) /etc/rc.d/init.d/zope3
%attr(755,root,root) %{_sbindir}/*
%dir %{zope_dir}
%dir %{zope_dir}/bin
%attr(755,root,root) %{zope_dir}/bin/*
%{zope_dir}/include
%{zope_dir}/lib
%dir %{zope_dir}/zopeskel
%dir %{zope_dir}/zopeskel/bin
%attr(755,root,root) %{zope_dir}/zopeskel/bin/*
%{zope_dir}/zopeskel/etc
%{zope_dir}/zopeskel/lib
%{zope_dir}/zopeskel/log
%{zope_dir}/zopeskel/var
%{zope_dir}/zopeskel/README.txt
%{py_sitedir}/zope/app
%attr(775,root,zope) %dir /var/run/zope3
%attr(755,root,root) %dir /var/lib/zope3
%attr(775,root,root) %dir /var/lib/zope3/main
%dir /var/lib/zope3/main/bin
%attr(755,root,root) %dir /var/lib/zope3/main/bin/*
/var/lib/zope3/main/etc
/var/lib/zope3/main/lib
/var/lib/zope3/main/log
%attr(775,root,zope) %dir /var/lib/zope3/main/var
/var/lib/zope3/main/var/README.txt
/var/lib/zope3/main/README.txt
%attr(755,root,zope) %dir /var/log/zope3
%attr(775,root,zope) %dir /var/log/zope3/main
%attr(751,root,zope) %dir /etc/zope3
%attr(751,root,zope) %dir /etc/zope3/main
%attr(751,root,zope) %dir /etc/zope3/main/package-includes
%attr(640,root,zope) %dir /etc/zope3/main/*.conf
/etc/zope3/main/*.zcml
/etc/zope3/main/package-includes/*.zcml
/etc/zope3/main/package-includes/README.txt
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/logrotate.d/zope3
%attr(640,root,root) /etc/sysconfig/zope3
%ghost /var/log/zope3/main/access.log
%ghost /var/log/zope3/main/transcript.log
%ghost /var/log/zope3/main/z3.log

%files -n python-zope
%defattr(644,root,root,755)
%{py_sitedir}/zope
%exclude %{py_sitedir}/zope/app
