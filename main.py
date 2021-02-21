#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""

"""


def gdal():
    import sys
    from osgeo import gdal
    from osgeo import ogr

    def raw_input():
        return "1 1 a"

    driverName = "ESRI Shapefile"
    drv = gdal.GetDriverByName(driverName)
    if drv is None:
        print("%s driver not available.\n" % driverName)
        sys.exit(1)

    ds = drv.Create("Output/test_point_out.shp", 0, 0, 0, gdal.GDT_Unknown)
    if ds is None:
        print("Creation of output file failed.\n")
        sys.exit(1)

    lyr = ds.CreateLayer("point_out", None, ogr.wkbPoint)
    if lyr is None:
        print("Layer creation failed.\n")
        sys.exit(1)

    field_defn = ogr.FieldDefn("Name", ogr.OFTString)
    field_defn.SetWidth(32)

    if lyr.CreateField(field_defn) != 0:
        print("Creating Name field failed.\n")
        sys.exit(1)

    # Expected format of user input: x y name
    linestring = raw_input()
    linelist = linestring.split()

    x = float(linelist[0])
    y = float(linelist[1])
    name = linelist[2]

    feat = ogr.Feature(lyr.GetLayerDefn())
    feat.SetField("Name", name)

    pt = ogr.Geometry(ogr.wkbPoint)
    pt.SetPoint_2D(0, x, y)

    feat.SetGeometry(pt)

    if lyr.CreateFeature(feat) != 0:
        print("Failed to create feature in shapefile.\n")
        sys.exit(1)

    feat.Destroy()

    # while len(linelist) == 3:
    #     x = float(linelist[0])
    #     y = float(linelist[1])
    #     name = linelist[2]
    #
    #     feat = ogr.Feature(lyr.GetLayerDefn())
    #     feat.SetField("Name", name)
    #
    #     pt = ogr.Geometry(ogr.wkbPoint)
    #     pt.SetPoint_2D(0, x, y)
    #
    #     feat.SetGeometry(pt)
    #
    #     if lyr.CreateFeature(feat) != 0:
    #         print("Failed to create feature in shapefile.\n")
    #         sys.exit(1)
    #
    #     feat.Destroy()
    #
    #     linestring = raw_input()
    #     linelist = linestring.split()

    ds = None


def wntr():
    """
    The following example demonstrates how to import WNTR, generate a water network
    model from an INP file, simulate hydraulics, and plot simulation results on the network.
    """
    import wntr

    # Create a water network model
    inp_file = 'Data/WNTR/networks/Net3.inp'
    wn = wntr.network.WaterNetworkModel(inp_file)

    # Graph the network
    wntr.graphics.plot_network(wn, title=wn.name)

    # Simulate hydraulics
    sim = wntr.sim.EpanetSimulator(wn)
    results = sim.run_sim()

    # Plot results on the network
    pressure_at_5hr = results.node['pressure'].loc[5 * 3600, :]
    wntr.graphics.plot_network(wn, node_attribute=pressure_at_5hr, node_size=30,
                               title='Pressure at 5 hours')


def main():
    """ Main program """
    # Code goes over here.
    a = "a"

    # wntr()
    gdal()

    return 0


if __name__ == "__main__":
    main()
