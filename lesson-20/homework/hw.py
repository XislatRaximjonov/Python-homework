import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("chinook.db")

# Load required tables
customers = pd.read_sql("SELECT * FROM Customer", conn)
invoices = pd.read_sql("SELECT * FROM Invoice", conn)
invoice_items = pd.read_sql("SELECT * FROM InvoiceLine", conn)
tracks = pd.read_sql("SELECT * FROM Track", conn)

conn.close()


# Merge customers with invoices
customer_invoices = customers.merge(
    invoices,
    on="CustomerId",
    how="inner"
)

# Calculate total spent per customer
total_spent = customer_invoices.groupby(
    ["CustomerId", "FirstName", "LastName"]
)["Total"].sum().reset_index()

total_spent.rename(columns={"Total": "TotalSpent"}, inplace=True)


top_5_customers = total_spent.sort_values(
    by="TotalSpent",
    ascending=False
).head(5)

print(top_5_customers)


invoice_tracks = invoice_items.merge(
    tracks[["TrackId", "AlbumId"]],
    on="TrackId",
    how="inner"
)

# Add CustomerId
invoice_tracks = invoice_tracks.merge(
    invoices[["InvoiceId", "CustomerId"]],
    on="InvoiceId",
    how="inner"
)

album_track_counts = tracks.groupby("AlbumId").size().reset_index(name="TotalTracks")


customer_album_tracks = invoice_tracks.groupby(
    ["CustomerId", "AlbumId"]
).TrackId.nunique().reset_index(name="TracksBought")

customer_album_tracks = customer_album_tracks.merge(
    album_track_counts,
    on="AlbumId",
    how="left"
)


# Flag full album purchases
customer_album_tracks["FullAlbum"] = (
    customer_album_tracks["TracksBought"] == customer_album_tracks["TotalTracks"]
)

# Customer-level preference
customer_preference = customer_album_tracks.groupby("CustomerId")["FullAlbum"].any().reset_index()

customer_preference["Preference"] = customer_preference["FullAlbum"].apply(
    lambda x: "Full Album" if x else "Individual Tracks"
)


preference_summary = customer_preference["Preference"].value_counts(normalize=True) * 100

preference_summary = preference_summary.reset_index()
preference_summary.columns = ["PurchaseType", "Percentage"]

print(preference_summary)
