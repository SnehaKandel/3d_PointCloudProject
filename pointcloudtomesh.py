import numpy as np
import open3d as o3d
#create paths and load data
input_path="vidsample/dense/"
output_path="vidsample/meshoutput/"
dataname="fused.ply"
point_cloud= np.loadtxt(input_path+dataname,skiprows=1)
#Format to open3d usable objects
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(point_cloud[:,:3])
pcd.colors = o3d.utility.Vector3dVector(point_cloud[:,3:6]/255)
pcd.normals = o3d.utility.Vector3dVector(point_cloud[:,6:9])
#BPA STRATEGY
#radius determination
distances = pcd.compute_nearest_neighbor_distance()
avg_dist = np.mean(distances)
radius = 3 * avg_dist
#computing the mehs
bpa_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(pcd,o3d.utility.DoubleVector([radius, radius * 2]))
#decimating the mesh
dec_mesh = bpa_mesh.simplify_quadric_decimation(100000)
#optional

dec_mesh.remove_degenerate_triangles()
dec_mesh.remove_duplicated_triangles()
dec_mesh.remove_duplicated_vertices()
dec_mesh.remove_non_manifold_edges()

#Strategy 2: Poisson' reconstruction
#computing the mesh
poisson_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=8, width=0, scale=1.1, linear_fit=False)[0]
#cropping
bbox = pcd.get_axis_aligned_bounding_box()
p_mesh_crop = poisson_mesh.crop(bbox)
#export
o3d.io.write_triangle_mesh(output_path+"_mbpaesh.obj", dec_mesh)
o3d.io.write_triangle_mesh(output_path+"p_mesh_c.obj", p_mesh_crop)
