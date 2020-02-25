<?xml version="1.0" encoding="UTF-8"?>
<!-- ~ Copyright (c) 2020. Bernard Bou <1313ou@gmail.com>. -->

<xsl:transform xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"
	xmlns:pwn="http://www.princeton.edu/wordnet/" 
	xmlns:ili="http://ili.org/ili/"
	xmlns:meta="https://github.com/globalwordnet/schemas/meta/" >

	<!-- <xsl:output doctype-system="http://globalwordnet.github.io/schemas/WN-LMF-relaxed-2.0.dtd" method="xml" indent="no" /> -->
	<xsl:output method="xml" indent="no" />

	<xsl:variable name="debug" select="false()" />
	<xsl:variable name="debug0" select="false()" />
	<xsl:variable name="debug_ns" select="false()" />
	<xsl:variable name="debug1" select="true()" />
	<xsl:variable name="debug2" select="true()" />
	<xsl:variable name="debug3" select="false()" />

	<!-- in ns -->
	<xsl:variable name="ns_dc" select="'http://purl.org/dc/elements/1.1/'" />

	<!-- out ns -->
	<xsl:variable name="ns_ili" select="'http://ili.org/ili/'" />
	<xsl:variable name="ns_meta" select="'https://github.com/globalwordnet/schemas/meta/'" />
	<xsl:variable name="ns_pwn" select="'http://www.princeton.edu/wordnet/'" />

	<xsl:template match="LexicalResource">
		<LexicalResource 
			xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
			xsi:schemaLocation=". https://x-englishwordnet.github.io/schemas/2.0/xEWN-LMF-2.0-relax_idrefs.xsd" 
			xmlns:pwn="http://www.princeton.edu/wordnet/" xmlns:ili="http://ili.org/ili/"
			xmlns:meta="https://github.com/globalwordnet/schemas/meta/">
			<xsl:apply-templates select="*" />
		</LexicalResource>
	</xsl:template>

	<xsl:template match="ILIDefinition">
		<xsl:element name="ili:Definition">
			<xsl:apply-templates select="text()" />
		</xsl:element>
	</xsl:template>

	<xsl:template match="*">

		<xsl:if test="$debug">
			<xsl:message>
				<xsl:text>ele </xsl:text>
				<xsl:value-of select="name()" />
			</xsl:message>
		</xsl:if>

		<xsl:copy>

			<!-- A T T R I B U T E S -->

			<xsl:for-each select="@*">
				<xsl:if test="$debug0">
					<xsl:message>
						<xsl:text>attr0 </xsl:text>
						<xsl:value-of select="name()" />
						<xsl:text> </xsl:text>
						<xsl:value-of select="namespace-uri()" />
					</xsl:message>
				</xsl:if>

				<xsl:choose>
					<xsl:when test="namespace-uri() = $ns_dc">
						<xsl:if test="$debug_ns">
							<xsl:message>
								<xsl:text>dc:attr </xsl:text>
								<xsl:value-of select="name()" />
							</xsl:message>
						</xsl:if>

						<xsl:choose>
							<xsl:when test="local-name()='identifier'">
								<xsl:attribute name="pwn:sensekey">
									<xsl:value-of select="." />
								</xsl:attribute>
								<xsl:if test="$debug1">
									<xsl:message>
										<xsl:text>dc:</xsl:text>
										<xsl:value-of select="local-name()" />
										<xsl:text> to pwn:sensekey</xsl:text>
									</xsl:message>
								</xsl:if>
							</xsl:when>
							<xsl:when test="local-name()='subject'">
								<xsl:attribute name="lexfile">
									<xsl:value-of select="." />
								</xsl:attribute>
								<xsl:if test="$debug1">
									<xsl:message>
										<xsl:text>dc:</xsl:text>
										<xsl:value-of select="local-name()" />
										<xsl:text> to lexfile</xsl:text>
									</xsl:message>
								</xsl:if>
							</xsl:when>
							<xsl:otherwise>
								<xsl:attribute name="{concat('meta:',local-name())}">
									<xsl:value-of select="." />
								</xsl:attribute>
								<xsl:if test="$debug1">
									<xsl:message>
										<xsl:text>dc:</xsl:text>
										<xsl:value-of select="local-name()" />
										<xsl:text> to meta:</xsl:text>
										<xsl:value-of select="local-name()" />
									</xsl:message>
								</xsl:if>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:when>

					<xsl:when test="namespace-uri() != ''">
						<xsl:message>
							<xsl:text>not captured ns </xsl:text>
							<xsl:value-of select="namespace-uri()" />
						</xsl:message>
					</xsl:when>

					<xsl:otherwise>
						<xsl:choose>
							<xsl:when test="local-name()='ili'">
								<xsl:attribute name="ili:id">
									<xsl:value-of select="." />
								</xsl:attribute>
								<xsl:if test="$debug2">
									<xsl:message>
										<xsl:value-of select="local-name()" />
										<xsl:text> to ili:id</xsl:text>
									</xsl:message>
								</xsl:if>
							</xsl:when>
							<xsl:when test="local-name()='status'">
								<xsl:attribute name="meta:status">
									<xsl:value-of select="." />
								</xsl:attribute>
								<xsl:if test="$debug2">
									<xsl:message>
										<xsl:value-of select="local-name()" />
										<xsl:text> to meta:status</xsl:text>
									</xsl:message>
								</xsl:if>
							</xsl:when>
							<xsl:when test="local-name()='note'">
								<xsl:attribute name="meta:note">
									<xsl:value-of select="." />
								</xsl:attribute>
								<xsl:if test="$debug2">
									<xsl:message>
										<xsl:value-of select="local-name()" />
										<xsl:text> to meta:note</xsl:text>
									</xsl:message>
								</xsl:if>
							</xsl:when>
							<xsl:when test="local-name()='confidenceScore'">
								<xsl:attribute name="meta:confidenceScore">
									<xsl:value-of select="." />
								</xsl:attribute>
								<xsl:if test="$debug2">
									<xsl:message>
										<xsl:value-of select="local-name()" />
										<xsl:text> to meta:confidenceScore</xsl:text>
									</xsl:message>
								</xsl:if>
							</xsl:when>

							<xsl:otherwise>
								<xsl:copy>
									<xsl:value-of select="." />
								</xsl:copy>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:for-each>

			<!-- S U B N O D E S -->

			<xsl:for-each select="node()">
				<xsl:apply-templates select="." />
			</xsl:for-each>

		</xsl:copy>
	</xsl:template>

	<xsl:template match="@*">
		<xsl:value-of select="." />
	</xsl:template>

	<xsl:template match="text()">
		<xsl:if test="$debug3">
			<xsl:message>
				<xsl:text>text </xsl:text>
				<xsl:value-of select="." />
			</xsl:message>
		</xsl:if>
		<xsl:copy>
			<xsl:value-of select="." />
		</xsl:copy>
	</xsl:template>

	<xsl:template match="comment()">
		<xsl:if test="$debug3">
			<xsl:message>
				<xsl:text>comment </xsl:text>
				<xsl:value-of select="." />
			</xsl:message>
		</xsl:if>
		<xsl:copy>
			<xsl:value-of select="." />
		</xsl:copy>
	</xsl:template>

</xsl:transform>
